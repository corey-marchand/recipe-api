from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from .models import Recipes
from .serializers import RecipesSerializer

# Create your views here.
class RecipesList(ListCreateAPIView):
    queryset = Recipes.objects.all()
    serializer_class = RecipesSerializer

class RecipesDetail(RetrieveUpdateAPIView):
    queryset = Recipes.objects.all()
    serializer_class = RecipesSerializer