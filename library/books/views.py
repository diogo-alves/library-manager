from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from .filters import BookFilter
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer


class AuthorPagination(PageNumberPagination):
    page_size = 10


class AuthorListAPIView(ListAPIView):
    queryset = Author.objects.all()
    pagination_class = AuthorPagination
    serializer_class = AuthorSerializer
    search_fields = ['name']


class BookViewSet(ModelViewSet):
    queryset = Book.objects.prefetch_related('authors')
    filter_backends = [DjangoFilterBackend]
    filterset_class = BookFilter
    serializer_class = BookSerializer
