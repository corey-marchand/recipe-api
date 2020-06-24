from rest_framework import serializers
from .models import Recipes

class RecipesSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','title','body','author', 'created_at',)
        model = Recipes