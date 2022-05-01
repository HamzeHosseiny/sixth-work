from django.shortcuts import render
from .models import Article
# Create your views here.

def detail_view(request, id = None):
    article = None
    if id is not None:
        article = Article.objects.get(id = id)
    
    context = {
        Article : article
    }
    
    return render(request, 'detail.html', context)