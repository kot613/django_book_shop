from django import forms


class SearchForm(forms.ModelForm):
    """ Форма підпису на новини"""

    class Meta:
        fields = ('email',)
        widgets = {'email': forms.TextInput(attrs={'class': "form-control"})}