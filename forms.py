from django import forms
from django.contrib.auth.models import User


from .models import *

class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields='__all__'

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields='__all__'