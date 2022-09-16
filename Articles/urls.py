from django.urls import path
from .views import *

app_name = 'Articles'
urlpatterns = [
    path('search/', search_view, name = 'search'),
    path('create/', Article_create_view, name = 'create'),
    path('article/<slug:slug>/', detail_view, name = 'detail'),
    ]