from django.urls import reverse

from rest_framework import status

from ..serializers import BookSerializer


class TestAuthorListAPIView:

    def test_author_list_should_be_paginated(self, client, authors):
        url = reverse('books:author-list')
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data['results']) == 10
        assert response.data['count'] == 15

    def test_author_list_should_allow_search_by_author_name(self, client, authors):
        url = reverse('books:author-list')
        payload = {'search': 'andrade'}
        response = client.get(url, data=payload)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 2


class TestBookViewSet:

    def test_list(self, client, books):
        url = reverse('books:book-list')
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 5

    def test_list_should_allow_filtering_by_name(self, client, books):
        url = reverse('books:book-list')
        payload = {'name__icontains': 'vidas secas'}
        response = client.get(url, data=payload)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 2

    def test_list_should_allow_filtering_by_publication_year(self, client, books):
        url = reverse('books:book-list')
        payload = {'publication_year': 1880}
        response = client.get(url, data=payload)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1

    def test_list_should_allow_filtering_by_edition(self, client, books):
        url = reverse('books:book-list')
        payload = {'edition': 1}
        response = client.get(url, data=payload)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 4

    def test_list_should_allow_filtering_by_author(self, client, books):
        url = reverse('books:book-list')
        payload = {'authors__name__icontains': 'Machado'}
        response = client.get(url, data=payload)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 2

    def test_list_should_allow_composite_filtering(self, client, books):
        url = reverse('books:book-list')
        payload = {
            'name__icontains': 'Vidas',
            'publication_year': 1938,
            'edition': 1,
            'authors__name__icontains': 'Graciliano'
        }
        response = client.get(url, data=payload)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1

    def test_create(self, client, author):
        url = reverse('books:book-list')
        payload = {
            'name': 'S. Bernardo',
            'publication_year': 1934,
            'edition': 1,
            'authors': [author.pk]
        }
        response = client.post(url, data=payload)
        assert response.status_code == status.HTTP_201_CREATED

    def test_retrieve(self, client, book):
        url = reverse('books:book-detail', kwargs={'pk': book.pk})
        response = client.get(url)
        serializer = BookSerializer(book)
        assert response.status_code == status.HTTP_200_OK
        assert response.data == serializer.data

    def test_update(self, client, book):
        url = reverse('books:book-detail', kwargs={'pk': book.pk})
        payload = {
            'name': book.name,
            'publication_year': 1947,
            'edition': 2,
            'authors': list(book.authors.values_list('id', flat=True))
        }
        response = client.put(url, data=payload, content_type='application/json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['publication_year'] == payload['publication_year']
        assert response.data['edition'] == payload['edition']

    def test_partial_update(self, client, book):
        url = reverse('books:book-detail', kwargs={'pk': book.pk})
        payload = {'edition': 2}
        response = client.patch(url, data=payload, content_type='application/json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['edition'] == payload['edition']

    def test_delete(self, client, book):
        url = reverse('books:book-detail', kwargs={'pk': book.pk})
        response = client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
