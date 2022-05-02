from django.shortcuts import render
from Articles.models import Article

def home(request):
    
    Articles = Article.objects.all()
    
    context = {
        'Articles' : Articles,
    }
    
    return render(request, 'main/home.html', context)