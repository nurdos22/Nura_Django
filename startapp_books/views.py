from django.shortcuts import get_object_or_404
from django.views import generic
from django.core.cache import cache
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from . import models


@method_decorator(cache_page(60 * 10), name='dispatch')
class SearchBooksView(generic.ListView):
    template_name = 'book.html'
    context_object_name = 'query'

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        cache_key = f'search_books_{query}'
        books = cache.get(cache_key)

        if not books:
            books = list(models.Books.objects.filter(title__icontains=query))
            cache.set(cache_key, books, 60 * 10)

        return books

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context


class BookDetailView(generic.DetailView):
    template_name = 'book_detail.html'
    context_object_name = 'book_id'

    def get_object(self, *args, **kwargs):
        book_id = self.kwargs.get('id')
        cache_key = f'book_detail_{book_id}'
        book = cache.get(cache_key)

        if not book:
            book = get_object_or_404(models.Films, id=book_id)
            cache.set(cache_key, book, 60 * 30)

        return book


@method_decorator(cache_page(60 * 15), name='dispatch')
class BookListView(generic.ListView):
    template_name = 'book.html'
    context_object_name = 'query'
    model = models.Films

    def get_queryset(self, *args, **kwargs):
        cache_key = 'all_books'
        books = cache.get(cache_key)

        if not books:
            books = list(self.model.objects.all())
            cache.set(cache_key, books, 60 * 15)

        return books


