from django.urls import path
from . import views


urlpatterns = [
    path('', views.BookListView.as_view(), name="book"),
    path("book_list/<int:id>/", views.BookDetailView.as_view(), name="books_detail"),
    path("search/", views.SearchBooksView.as_view(), name="search"),
    path("film_list/<int:id>/", views.BookDetailView.as_view(), name="film_detail")


]