from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

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
    serializer_class = BookSerializer
