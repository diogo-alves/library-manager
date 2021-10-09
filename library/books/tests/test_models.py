from ..models import Author


class TestAuthor:

    def test_string_representation(self):
        author = Author(name='J. R. R. Tolkien')
        assert str(author) == author.name
