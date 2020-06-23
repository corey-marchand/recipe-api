from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

class Recipes(models.Model):
    title = models.CharField(max_length=64)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    body = models.TextField()