from django import forms
from django.contrib.auth import password_validation

class LoginForm(forms.Form):
    username = forms.CharField()
    #email = forms.CharField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput)
    

