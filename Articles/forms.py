from .models import Article
from django import forms

# form by ModelForm. just this take form.save() attribute
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title','content']

# basic django standard form. just this needs to get data throut the cleaned_data.get function.
class OldArticleForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField(widget=forms.Textarea)
