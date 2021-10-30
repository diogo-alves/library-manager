import django_filters as filters

from .models import Book


class BookFilter(filters.FilterSet):

    class Meta:
        model = Book
        fields = {
            'name': ['icontains'],
            'publication_year': ['exact'],
            'edition': ['exact'],
            'authors__name': ['icontains']
        }
