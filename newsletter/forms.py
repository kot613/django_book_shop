from django import forms
from .models import Newsletter


class EmailForm(forms.ModelForm):
    """ Форма підпису на новини"""

    class Meta:
        model = Newsletter
        fields = ('email',)
        widgets = {'email': forms.TextInput(attrs={'class': "form-control", 'placeholder': "Ваша e-пошта"})}
