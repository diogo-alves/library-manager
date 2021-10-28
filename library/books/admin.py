from django.contrib import admin
from django.utils.text import get_text_list

from .models import Author, Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('id', 'name')


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'edition', 'publication_year', 'authors_names',
    )
    list_display_links = ('id', 'name',)
    list_filter = ('edition', 'publication_year',)
    search_fields = ('id', 'name', 'authors__name',)
    autocomplete_fields = ('authors',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.prefetch_related('authors')

    @admin.display(description='authors')
    def authors_names(self, obj):
        names = list(obj.authors.values_list('name', flat=True))
        return get_text_list(names, last_word='and')
