from django.db import models
import random
from django.utils.text import slugify
from django.db.models.signals import pre_save, post_save
# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length = 255)
    slug = models.SlugField(blank = True, null = True)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add = True)
    updated_time = models.DateTimeField(auto_now= True)
    published = models.DateField(auto_now_add = False, auto_now = False, null = True, blank = True)
    

    #def save(self, *args, **kwargs):
        #if self.slug == None:
          # self.slug = slugify(self.title)
        #super(Article, self).save(*args, **kwargs)

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