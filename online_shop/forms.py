from django import forms
from online_shop.models import Product, Coments
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'new_price', 'description']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Coments
        fields = ['name', 'email', 'body']



class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email']
