from django import forms
from .models import Meeting

class ProductForm(forms.ModelForm):
    class Meta:
        model=Meeting
        fields='__all__'

