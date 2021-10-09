from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'author'
        ordering = ['name']

    def __str__(self):
        return self.name
