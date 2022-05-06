from django.db import models
from django.forms import CharField

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length = 255)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add = True)
    updated_time = models.DateTimeField(auto_now= True)
    published = models.DateField(auto_now_add = False, auto_now = False, null = True, blank = True)
    