from django import forms
from .models import *

from django.contrib.auth.models import User


class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['order_by', 'shipping_address', 'mobile', 'email']


class CustomerRegistrationForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.CharField(widget=forms.EmailInput())

    class Meta:
        model = Customer
        fields = ['username', 'password', 'email', 'full_name', 'address']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(
                'Customer with this name is already exists')
        return username

class CustomerLoginForm(forms.Form):

    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())


class AdminLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
