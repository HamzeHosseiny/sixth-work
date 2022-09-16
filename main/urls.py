from django.contrib import admin
from django.urls import path, include
from .views import home
from account.views import login_view, logout_view, Register_view

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('Recipes/', include('Recipes.urls')),
    path('Articles/', include('Articles.urls')),
    path('Profiles/', include('account.urls')),
]
