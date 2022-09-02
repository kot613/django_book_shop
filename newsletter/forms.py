from django import forms
from .models import Newsletter
from django.utils.translation import gettext as _


class EmailForm(forms.ModelForm):
    """ Форма підпису на новини"""

    class Meta:
        model = Newsletter
        fields = ('email',)
        widgets = {'email': forms.TextInput(attrs={'class': "form-control", 'placeholder': "E-mail"})}
