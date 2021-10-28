import pytest

from ..models import Author, Book


@pytest.fixture
def author(db):
    return Author.objects.create(name='Graciliano Ramos')

@pytest.fixture
def authors(db):
    Author.objects.bulk_create([
        Author(name='José de Alencar'),
        Author(name='Machado de Assis'),
        Author(name='Euclides da Cunha'),
        Author(name='Lima Barreto'),
        Author(name='Monteiro Lobato'),
        Author(name='Manuel Bandeira'),
        Author(name='Graciliano Ramos'),
        Author(name='Mário de Andrade'),
        Author(name='Cecília Meireles'),
        Author(name='Carlos Drummond de Andrade'),
        Author(name='Érico Veríssimo'),
        Author(name='Guimarães Rosa'),
        Author(name='Jorge Amado'),
        Author(name='Vinicius de Moraes'),
        Author(name='Clarice Lispector'),
    ])

@pytest.fixture
def book(db, author):
    new_book = Book.objects.create(
        name='Vidas Secas',
        edition=1,
        publication_year=1938,
    )
    new_book.authors.add(author)
    return new_book
