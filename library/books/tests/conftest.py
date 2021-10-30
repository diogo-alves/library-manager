import pytest
from model_bakery import baker


@pytest.fixture
def author(db):
    return baker.make('Author', name='Graciliano Ramos')

@pytest.fixture
def authors(db):
    baker.make('Author', name='José de Alencar')
    baker.make('Author', name='Machado de Assis')
    baker.make('Author', name='Euclides da Cunha')
    baker.make('Author', name='Lima Barreto')
    baker.make('Author', name='Monteiro Lobato')
    baker.make('Author', name='Manuel Bandeira')
    baker.make('Author', name='Graciliano Ramos')
    baker.make('Author', name='Mário de Andrade')
    baker.make('Author', name='Cecília Meireles')
    baker.make('Author', name='Carlos Drummond de Andrade')
    baker.make('Author', name='Érico Veríssimo')
    baker.make('Author', name='Guimarães Rosa')
    baker.make('Author', name='Jorge Amado')
    baker.make('Author', name='Vinicius de Moraes')
    baker.make('Author', name='Clarice Lispector')

@pytest.fixture
def book(author):
    return baker.make(
        'Book',
        name='Vidas Secas',
        publication_year=1938,
        edition=1,
        authors=[author]
    )

@pytest.fixture
def books(db):
    author1 = baker.make('Author', name='Graciliano Ramos')
    author2 = baker.make('Author', name='Machado de Assis')

    baker.make(
        'Book',
        name='Vidas Secas',
        publication_year=1938,
        edition=1,
        authors=[author1]
    )
    baker.make(
        'Book',
        name='Vidas Secas',
        publication_year=1947,
        edition=2,
        authors=[author1]
    )
    baker.make(
        'Book',
        name='S. Bernardo',
        publication_year=1934,
        edition=1,
        authors=[author1]
    )
    baker.make(
        'Book',
        name='Dom Casmurro',
        publication_year=1899,
        edition=1,
        authors=[author2]
    )
    baker.make(
        'Book',
        name='Memórias Póstumas de Brás Cubas',
        publication_year=1880,
        edition=1,
        authors=[author2]
    )
