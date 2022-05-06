from atexit import register
from django.contrib import admin
from Articles.models import Article
# Register your models here.

class AricleAdmin(admin.ModelAdmin):
    list_display = ['title', 'id', 'content', 'created_time', 'updated_time']
    list_search = ['content']

admin.site.register(Article, AricleAdmin)