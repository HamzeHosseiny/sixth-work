from django.urls import path
from .views import *

app_name = 'Recipes'
urlpatterns = [
    path('', Recipes_List_View, name = 'list'),
    path('detail/<int:id>/', Recipes_Detail_View, name = 'detail'),
    path('create/', Recipes_Create_View, name = 'create'),
    path('update/<int:id>', Recipes_Update_View, name = 'update'),
    path('delete/', Recipes_Delete_View, name = 'delete'),
]