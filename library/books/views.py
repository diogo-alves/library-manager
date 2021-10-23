from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination

from .models import Author
from .serializers import AuthorSerializer


class AuthorPagination(PageNumberPagination):
    page_size = 10


class AuthorListAPIView(ListAPIView):
    queryset = Author.objects.all()
    pagination_class = AuthorPagination
    serializer_class = AuthorSerializer
    search_fields = ['name']
