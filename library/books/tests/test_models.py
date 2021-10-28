from ..models import Author, Book


class TestAuthorModel:

    def test_string_representation(self, author):
        assert str(author) == author.name


class TestBookModel:

    def test_string_representation(self, book):
        assert str(book) == f'{book.name} ({book.publication_year})'
