from django.urls import path
from .views import AllCategoryFilmView, FantasticCategoryFilmView, ComedyCategoryFilmView


urlpatterns = [
    path('films/all/', AllCategoryFilmView.as_view(), name='all_category_film'),
    path('films/fantastic/', FantasticCategoryFilmView.as_view(), name='fantastic_category_film'),
    path('films/comedy/', ComedyCategoryFilmView.as_view(), name='comedy_category_film'),
]