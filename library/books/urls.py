from django.urls import include, path

from rest_framework import routers

from .views import AuthorListAPIView, BookViewSet


app_name = 'books'
router = routers.SimpleRouter()
router.register('books', BookViewSet)

urlpatterns = [
    path('authors/', AuthorListAPIView.as_view(), name='author-list'),
    path('', include(router.urls)),
]
