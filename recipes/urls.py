from django.urls import path
from .views import RecipesList, RecipesDetail

urlpatterns = [
    path('', RecipesList.as_view()),
    path('<int:pk>/', RecipesDetail.as_view()),
]