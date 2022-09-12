from django.conf import settings
from django.db import models
from django.db.models import Q
from django.utils.text import slugify
from django.db.models.signals import pre_save, post_save

User = settings.AUTH_USER_MODEL

class ArticleQuerySet(models.QuerySet):
    def search(self, query=None):
        if query is None or query == "":
            return self.none()
        lookups = Q(title__icontains = query) | Q(content__icontains = query)
        return self.filter(lookups)

class ArticleManager(models.Manager):
    def get_queryset(self):
        return ArticleQuerySet(self.model, using = self._db)
    
    def search(self, query = None):
        return self.get_queryset().search(query = query)

class Article(models.Model):
    user = models.ForeignKey(User, blank = True, null = True, on_delete = models.SET_NULL)
    title = models.CharField(max_length = 255)
    slug = models.SlugField(blank = True, null = True)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add = True)
    updated_time = models.DateTimeField(auto_now= True)
    published = models.DateField(auto_now_add = False, auto_now = False, null = True, blank = True)
    
    objects = ArticleManager()

def slugify_instance_title(instance, save = False):
    slug = slugify(instance.title)
    instance.slug = slug
    qs = Article.objects.filter(slug = slug).exclude(id = instance.id)
    if qs.exists():
        instance.slug = f"{instance.slug}-{instance.id}"
    if save:
        instance.save()


def article_pre_save_receaver(sender, instance, *args, **kwargs):
    if instance.slug == None:
        slugify_instance_title(instance, save = False)
        
pre_save.connect(article_pre_save_receaver, Article)

# the save is happen here

def article_post_save_receaver(sender, instance, created, *args, **kwargs):
    if created:
        slugify_instance_title(instance, save = True)
        
post_save.connect(article_post_save_receaver, Article)