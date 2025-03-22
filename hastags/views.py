from django.views.generic import ListView
from .models import Post


class AllCategoryFilmView(ListView):
    model = Post
    template_name = 'tags/all_category_film.html'
    context_object_name = 'query'


class FantasticCategoryFilmView(ListView):
    model = Post
    template_name = 'tags/fantastic_category_film.html'
    context_object_name = 'query'

    def get_queryset(self):
        return Post.objects.filter(tags__name='Фантастика')


class ComedyCategoryFilmView(ListView):
    model = Post
    template_name = 'tags/comedy_category_film.html'
    context_object_name = 'query'

    def get_queryset(self):
        return Post.objects.filter(tags__name='Комедия')