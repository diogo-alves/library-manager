from rest_framework import serializers

from .models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ['id', 'name']


class BookSerializer(serializers.ModelSerializer):
    authors = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Author.objects.all()
    )

    class Meta:
        model = Book
        fields = ['id', 'name', 'publication_year', 'edition', 'authors']
