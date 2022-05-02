from django.shortcuts import render
from .models import Article
# Create your views here.

def detail_view(request, id = None):
    article = None
    if id is not None:
        article = Article.objects.get(id = id)
    
    context = {
        'Article' : article
    }
    
    return render(request, 'Articles/detail.html', context)

def search_view(request):
    
    queryset = request.GET #this is a dictionary <WSGI Queryset: {['q']:[the user search]}>
    q = queryset.get('q')
    try:
        q = int(q)
    except:
        q = None
    
    article = None
    
    if q is not None:
        
        try:
            article = Article.objects.get(id = q)
        except:
            article = None
    
    context = {
        'Article' : article
    }
    
    return render(request, 'Articles/search.html', context)

def Article_create_view(request):
    title = None
    content = None
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
    
    article = Article.objects.create(title = title, content = content)
    
    return render(request, 'Articles/Article-create.html')
