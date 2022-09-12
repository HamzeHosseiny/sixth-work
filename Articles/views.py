from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import redirect, render
from .forms import ArticleForm
from .models import Article
# Create your views here.

def detail_view(request, slug = None):
    article = None
    if slug is not None:
        article = Article.objects.get(slug = slug)
    
    context = {
        'Article' : article
    }
    
    return render(request, 'Articles/detail.html', context)

def search_view(request):
    query = request.GET.get('q')#this is a dictionary <WSGI Queryset: {['q']:[the user search]}>
    article = Article.objects.search(query = query)  
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
        return redirect('detail', slug = article.slug)
    return render(request, 'Articles/Article-create.html', context = context)