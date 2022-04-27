from django.urls import path
from .views import book_view, book_detail

urlpatterns = [
    path("", book_view, name="book-list"),
    path("<int:pk>/", book_detail, name="book-detail"),
]