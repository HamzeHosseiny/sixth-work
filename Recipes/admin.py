from django.contrib import admin
from .models import Recipe, RecipeIngredient

# Register your models here.

class RecipeIngredientInline(admin.StackedInline):
    model = RecipeIngredient
    extra = 0
    readonly_fields = ['quantity_as_float', 'as_mks', 'as_imperial']

class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline]
    model = Recipe
    list_display = ['name', 'descriptions']
    readonly_fields = ['timestamps', 'update']
    raw_id_fields = ['user']

admin.site.register(Recipe, RecipeAdmin)