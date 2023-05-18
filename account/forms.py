from django import forms

class LoginForm(forms.Form):
    username = forms.CharField()
    #email = forms.CharField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput)