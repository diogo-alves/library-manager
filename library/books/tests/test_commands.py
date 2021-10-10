from io import StringIO

import pytest

from django.core.management import call_command
from django.core.management.base import CommandError

from ..models import Author


@pytest.fixture
def authors_names():
    return [
        'Luciano Ramalho',
        'Osvaldo Santana Neto',
        'David Beazley',
        'Chetan Giridhar',
        'Brian K. Jones',
        'J.K Rowling'
    ]

@pytest.fixture
def valid_csv(tmp_path, authors_names):
    file = tmp_path / 'authors.csv'
    file_header = ['name']
    file.write_text('\n'.join(file_header + authors_names))
    return file

@pytest.fixture
def invalid_csv(tmp_path, authors_names):
    file = tmp_path / 'authors.csv'
    file.write_text('\n'.join(authors_names))
    return file


class TestImportAuthors:

    def test_import_authors_from_csv_file(self, db, valid_csv, authors_names):
        assert Author.objects.count() == 0
        call_command('import_authors', valid_csv)
        assert Author.objects.count() == 6
        names = Author.objects.values_list('name', flat=True).order_by('id')
        assert list(names) == authors_names

    @pytest.mark.parametrize('batch_size, bulk_create_calls', [(1, 6), (2, 3), (3, 2), (6, 1)])
    def test_import_authors_with_custom_batch_sizes(self, mocker, valid_csv, batch_size, bulk_create_calls):
        bulk_create = mocker.patch.object(Author.objects, 'bulk_create')
        call_command('import_authors', valid_csv, batch_size=batch_size)
        assert bulk_create.call_count == bulk_create_calls

    def test_import_authors_should_raise_an_error_when_csv_file_is_not_provided(self):
        error_message = 'No csv file specified. Please provide the path to the csv file.'
        with pytest.raises(CommandError, match=error_message):
            call_command('import_authors')

    def test_import_authors_should_raise_an_error_when_csv_file_does_not_exist(self):
        error_message = 'The file "non_existent_file.csv" is not a valid csv file!'
        with pytest.raises(CommandError, match=error_message):
            call_command('import_authors', 'non_existent_file.csv')

    def test_import_authors_should_raise_an_error_when_csv_file_does_not_have_a_name_column(self, invalid_csv):
        error_message = 'Invalid file format! No "name" column found in csv header.'
        with pytest.raises(CommandError, match=error_message):
            call_command('import_authors', invalid_csv)
