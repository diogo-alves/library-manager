from django.urls import path

from .views import AuthorListAPIView


app_name = 'books'

urlpatterns = [
    path('authors/', AuthorListAPIView.as_view(), name='author-list')
]
