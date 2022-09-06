from django import forms
from .models import Comment


class SearchForm(forms.ModelForm):
    """ Форма підпису на новини"""

    class Meta:
        fields = ('email',)
        widgets = {'email': forms.TextInput(attrs={'class': "form-control"})}


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['message']
        widgets = {'message': forms.Textarea(attrs={'class': "form-control"})
                   }