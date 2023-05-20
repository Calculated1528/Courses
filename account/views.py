from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout,update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from .forms import LoginForm,UserRegistrationForm
from shop.views import index
from django.contrib.auth.views import PasswordResetView


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return index(request)
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login or password')
    else:
        form = LoginForm()
    return render(request, 'account/registration/login.html', {'form': form})


def user_logout(request):
    user_logout = logout(request)
    return render(request,'account/registration/logout.html')

def account(request):
    return render(request, 'account/account.html')


def change_password(request):
    template_name = 'account/registration/change_passsword.html'
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return render(request, 'account/registration/change_password_done.html', {'form': form})
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'account/registration/change_password.html', {'form': form})


def registration(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'account/registration/registration_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/registration/registration.html', {'user_form': user_form})