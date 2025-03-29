from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .models import Recipe, Ingredient

class RecipeListView(ListView):
    model = Recipe
    template_name = "recipes/recipe_list.html"
    context_object_name = "recipes"

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "recipes/recipe_detail.html"
    context_object_name = "recipe"

class RecipeCreateView(CreateView):
    model = Recipe
    template_name = "recipes/recipe_form.html"
    fields = ['title', 'description']
    success_url = reverse_lazy('recipe-list')

class RecipeDeleteView(DeleteView):
    model = Recipe
    template_name = "recipes/recipe_confirm_delete.html"
    success_url = reverse_lazy('recipe-list')

class IngredientCreateView(CreateView):
    model = Ingredient
    template_name = "recipes/ingredient_form.html"
    fields = ['name', 'quantity', 'recipe']

    def get_success_url(self):
        return reverse_lazy('recipe-detail', kwargs={'pk': self.object.recipe.id})

