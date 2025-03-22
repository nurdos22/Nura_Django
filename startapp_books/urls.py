from django.urls import path
from . import views


urlpatterns = [
    path("", views.BookListView.as_view(), name="books"),
    path("book_list/<int:id>/", views.BookDetailView.as_view(), name="books_detail"),
    path("search/", views.SearchBooksView.as_view(), name="search"),
]