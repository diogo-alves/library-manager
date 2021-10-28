from django.core.validators import MaxValueValidator
from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'author'
        ordering = ['name']

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=100)
    edition = models.PositiveSmallIntegerField()
    publication_year = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(2999)
        ]
    )
    authors = models.ManyToManyField(Author, related_name='books')

    class Meta:
        db_table = 'book'
        ordering = ['name', 'edition']

    def __str__(self):
        return f'{self.name} ({self.publication_year})'
