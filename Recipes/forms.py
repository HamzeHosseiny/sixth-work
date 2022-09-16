from django import forms
from .models import Recipe, RecipeIngredient

class RecipeForm(forms.ModelForm):
    requaired_css_class = 'requaired-field'
    name = forms.CharField(help_text = "This is your help<a href='#' >Contact Us</a>")
    class Meta:
        model = Recipe
        fields = ['name', 'descriptions', 'directions',]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            new_data = {
                "placeholder" : f"Recipe {str(field)}",
                "class" : "form-control"
            }
            self.fields[str(field)].widget.attrs.update(new_data)
        self.fields['descriptions'].widget.attrs.update({"rows" : 3})
        self.fields['directions'].widget.attrs.update({"rows" : 2})
        
        

class RecipeIngredientForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = ['name', 'quantity', 'unit',]
