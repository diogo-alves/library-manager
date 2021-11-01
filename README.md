# Library Manager REST API

 [![License](https://img.shields.io/badge/license-MIT-brightgreen.svg)](https://img.shields.io/badge/license-MIT-brightgreen)


## Description

A REST API to manage books and authors data. It was based on [this challenge](https://github.com/olist/work-at-olist) by [Olist company](https://olist.com/).


## Live preview

This project was deployed on [Heroku](https://www.heroku.com/) and is available [here](https://library-manager-api.herokuapp.com/api).

[![](https://i.imgur.com/kXBkdXK.png)](https://library-manager-api.herokuapp.com/api)


## Prerequisites

Before you start, install **[Git](https://git-scm.com/)** and **[Poetry](https://python-poetry.org/)**. Optionally, if you want to dockerize this application, install **[Docker](https://docs.docker.com/engine/install/)** and **[Docker Compose](https://docs.docker.com/compose/install/)**.


## Getting Started

1. Clone this repository
```shell
git clone git@github.com:diogo-alves/library-manager.git
```

2. Go to project directory
```shell
cd library-manager
```


## Executing the project

### Running locally:

1. Install the requirements
```shell
poetry install
```
2. Activate virtualenv
```shell
poetry shell
```
3. Update the database structure
```shell
python manage.py migrate
```
4. Start the web server
```shell
python manage.py runserver
```


### Running with docker:

1. Start web server and database services
```shell
docker-compose up -d
```
2. Update the database structure
```shell
docker-compose exec web python manage.py migrate
```

**With the web server running access the API at `http://localhost:8000/api/`**


## Testing

#### Running locally:
```shell
pytest
```

#### Running with docker:
```shell
docker-compose exec web pytest
```


## API endpoints

This project implements the OpenAPI Specification (formerly Swagger Specification). The full documentation can be accessed at `http://localhost:8000/api/`.

### Authors
| Action                          | HTTP VERB | Endpoint                                  |
| --------------------------------|:---------:|-------------------------------------------|
| List authors                    | `GET`     | api/authors/                              |
| Search author by name           | `GET`     | api/authors/?search={name}                |
| Paginate authors list           | `GET`     | api/authors/?page={number}                |


### Books
| Action                          | HTTP VERB | Endpoint                                  |
| --------------------------------|:---------:|-------------------------------------------|
| List books                      | `GET`     | api/books/                                |
| Filter books by name            | `GET`     | api/books/?name__icontains={name}         |
| Filter books by publication year| `GET`     | api/books/?publication_year={year}        |
| Filter books by editon          | `GET`     | api/books/?edition={edition}              |
| Filter books by author name     | `GET`     | api/books/?authors__name__icontains={name}|
| Create a book                   | `POST`    | api/books/                                |
| Retrieve book                   | `GET`     | api/books/{id}/                           |
| Update/Replace book             | `PUT`     | api/books/{id}/                           |
| Update/Modify book              | `PATCH`   | api/books/{id}/                           |
| Delete book                     | `DELETE`  | api/books/{id}/                           |


## Importing authors

A django management command was created to import a CSV file with authors names. The file must follow the format:
```csv
name
Luciano Ramalho
Osvaldo Santana Neto
David Beazley
Chetan Giridhar
Brian K. Jones
J.K Rowling
```

To import run:
```shell
python manage.py import_authors authors.csv
# or
docker-compose exec web python manage.py import_authors authors.csv
```

## Built With

- **[Django](https://www.djangoproject.com/)**
- **[Django Rest Framework](https://www.django-rest-framework.org/)**
- **[drf-spectacular](https://drf-spectacular.readthedocs.io/)**
- **[Django Filter](https://pypi.org/project/django-filter/)**
- **[PostgreSQL](https://www.postgresql.org/)**
- **[Pytest](https://docs.pytest.org/)**
- **[Python](https://www.python.org/)**
- **[Python Decouple](https://pypi.org/project/python-decouple/)**


## Environment
- **[Docker](https://docs.docker.com/engine/install/)**
- **[Docker Compose](https://docs.docker.com/compose/install/)**
- **[Git](https://git-scm.com/)**
- **[Poetry](https://python-poetry.org/)**


## License
This project is licensed under the terms of the [MIT License](./LICENSE).
