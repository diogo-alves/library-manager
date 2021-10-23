from ..models import Author


class TestAuthor:

    def test_string_representation(self, author):
        assert str(author) == author.name
