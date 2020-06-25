from .models import Recipes
from .serializers import RecipesSerializer
from rest_framework import generics
from .permissions import isAuthorOrReadOnly

# Create your views here.
class RecipesList(generics.ListCreateAPIView):
    queryset = Recipes.objects.all()
    serializer_class = RecipesSerializer

class RecipesDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (isAuthorOrReadOnly,)
    queryset = Recipes.objects.all()
    serializer_class = RecipesSerializer
