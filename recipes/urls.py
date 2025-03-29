from django.urls import path
from .views import RecipeListView, RecipeDetailView, RecipeCreateView, RecipeDeleteView, IngredientCreateView

urlpatterns = [
    path('', RecipeListView.as_view(), name='recipe-list'),
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name='recipe-detail'),
    path('recipe/new/', RecipeCreateView.as_view(), name='recipe-create'),
    path('recipe/<int:pk>/delete/', RecipeDeleteView.as_view(), name='recipe-delete'),
    path('recipe/<int:pk>/add-ingredient/', IngredientCreateView.as_view(), name='ingredient-create'),
]
