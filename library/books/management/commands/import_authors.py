import csv
import time
from itertools import islice
from pathlib import Path

from django.core.management.base import BaseCommand, CommandError

from ...models import Author

DEFAULT_BATCH_SIZE = 100_000


class Command(BaseCommand):
    help = 'Imports authors from a csv file. Expects names of authors.'
    missing_args_message = (
        'No csv file specified. Please provide the path to the csv file.'
    )

    def add_arguments(self, parser):
        parser.add_argument('file', type=Path, metavar='FILE', help='Path to csv file.')
        parser.add_argument(
            '-b',
            '--batch-size',
            type=int,
            default=DEFAULT_BATCH_SIZE,
            help=(
                'Controls how many authors can be created per query. '
                f'Default value is {DEFAULT_BATCH_SIZE}.'
            ),
        )

    def handle(self, *args, **options):
        start_time = time.time()
        file = options.get('file')
        authors = self.read_csv(file)
        batch_size = options.get('batch_size')
        self.save_authors(authors, batch_size)
        elapsed_time = time.time() - start_time
        self.stdout.write(
            self.style.SUCCESS(
                f'Authors were successfully imported! Finished in {elapsed_time:.0f}s.'
            )
        )

    def read_csv(self, file):
        if not file.is_file() or file.suffix.lower() != '.csv':
            raise CommandError(f'The file "{file}" is not a valid csv file!')
        with file.open() as csv_file:
            csv_reader = csv.DictReader(csv_file)
            if 'name' not in csv_reader.fieldnames:
                raise CommandError(
                    'Invalid file format! No "name" column found in csv header.'
                )
            yield from self.generate_authors(csv_reader)

    def generate_authors(self, reader):
        for row in reader:
            name = row.get('name')
            yield Author(name=name)

    def save_authors(self, authors, batch_size):
        while True:
            batch = list(islice(authors, batch_size))
            if not batch:
                break
            Author.objects.bulk_create(batch, batch_size, ignore_conflicts=True)

