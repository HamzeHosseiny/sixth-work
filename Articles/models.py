from django.db import models
from django.forms import CharField

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length = 255)
    content = models.TextField()
    
    