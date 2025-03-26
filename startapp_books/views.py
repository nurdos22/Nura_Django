from django.shortcuts import get_object_or_404
from django.views import generic
from django.views import generic
from . import models


class SearchBooksView(generic.ListView):
    template_name = 'book.html'
    context_object_name = 'query'

    def get_queryset(self):
        return models.Books.objects.filter(title__icontains=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context


class BookDetailView(generic.DetailView):
    template_name = 'book_detail.html'
    context_object_name = 'book_id'

    def get_object(self, *args, **kwargs):
        return get_object_or_404(models.Films, id=self.kwargs.get('id'))


class BookListView(generic.ListView):
    template_name = 'book.html'
    context_object_name = 'query'
    model = models.Films

    def get_queryset(self, *args, **kwargs):
        return self.model.objects.all()


