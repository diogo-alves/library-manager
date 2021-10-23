import pytest

from django.urls import reverse

from rest_framework import status


@pytest.mark.django_db
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
