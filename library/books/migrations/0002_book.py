# Generated by Django 3.2.8 on 2021-10-28 19:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('edition', models.PositiveSmallIntegerField()),
                ('publication_year', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(2999)])),
                ('authors', models.ManyToManyField(related_name='books', to='books.Author')),
            ],
            options={
                'db_table': 'book',
                'ordering': ['name', 'edition'],
            },
        ),
    ]
