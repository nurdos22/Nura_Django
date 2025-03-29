from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.BookListView.as_view(), name="book"),
    path("book_list/<int:id>/", views.BookDetailView.as_view(), name="books_detail"),
    path("search/", views.SearchBooksView.as_view(), name="search"),
    path("film_list/<int:id>/", views.BookDetailView.as_view(), name="film_detail")


]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)