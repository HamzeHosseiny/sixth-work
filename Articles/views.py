from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .forms import ArticleForm
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

##@login_required
##def Article_create_view(request):
##    form = ArticleForm()
##    if request.method == "POST":
##        form = ArticleForm(request.POST)
##        if form.is_valid():
##            title = form.cleaned_data.get('title')
##            content = form.cleaned_data.get('content')
##            article = Article.objects.create(title = title, content = content)
##            form = ArticleForm()
##            created = True
##    
##    return render(request, 'Articles/Article-create.html', {'form': form})



@login_required
def Article_create_view(request):
    form = ArticleForm(request.POST or None)
    context = {'form' : form}
    if form.is_valid():
        article = form.save()
        created = True
        context['created'] = created
        context['article'] = article
    return render(request, 'Articles/Article-create.html', context = context)