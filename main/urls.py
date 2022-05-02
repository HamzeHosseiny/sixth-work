from django.contrib import admin
from django.urls import path
from .views import home
from Articles.views import detail_view, search_view, Article_create_view
from account.views import login_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('search/', search_view),
    path('create/', Article_create_view),
    path('article/<int:id>/', detail_view),
    path('login/', login_view)
]
