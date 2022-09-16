from django.shortcuts import render, get_object_or_404, redirect
from django.forms.models import modelformset_factory
from .models import Recipe, RecipeIngredient
from django.contrib.auth.decorators import login_required
from .forms import RecipeForm, RecipeIngredientForm

# Create your views here.
# CRUD ===> Create, Retrive, Update, Delete


@login_required
def Recipes_List_View(request):
    Recipes = Recipe.objects.filter(user = request.user)
    context = {
        'Recipe' : Recipes
    }
    return render(request, 'Recipes/Recipes_List.html', context)

@login_required
def Recipes_Detail_View(request, id = None):
    if id is not None:
        UR = get_object_or_404(Recipe, id = id, user = request.user)
    context = {
        'UserRecipe' : UR
    }
    return render(request, 'Recipes/Recipe_Detail.html', context)

@login_required
def Recipes_Create_View(request):
    form = RecipeForm(request.POST or None)
    context = {
        'form' : form,
    }
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        return redirect('Recipes:detail', id = obj.id)
    return render(request, 'Recipes/Recipe_Create_Update.html', context)

@login_required
def Recipes_Update_View(request, id = None):
    obj = get_object_or_404(Recipe, id = id, user = request.user)
    form = RecipeForm(request.POST or None, instance = obj)
    RecipeIngredientFormset = modelformset_factory(model = RecipeIngredient, form = RecipeIngredientForm, extra = 0)
    qs = obj.recipeingredient_set.all()
    formset = RecipeIngredientFormset(request.POST or None, queryset = qs)
    context = {
        'form' : form,
        'formset': formset,
        'object' : obj,
    }
    if all([form.is_valid(), formset.is_valid()]):
        parent = form.save(commit=False)
        parent.save()
        for form in formset:
            child = form.save(commit=False)
            if child.recipe is None:
                child.recipe = parent
            child.save()
        context['message'] = 'Your Data Is Saved.'
    return render(request, 'Recipes/Recipe_Create_Update.html', context)

@login_required
def Recipes_Delete_View(requset, id):
    pass