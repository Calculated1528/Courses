from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

#app_name = 'account'
urlpatterns = [
    path('', views.account, name='account'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('registration/',  views.registration, name='registration'),
    path('change_password', views.change_password, name='change_password'),

    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name = 'account/registration/password_reset.html',
        email_template_name='account/registration/password_reset_email.html'), 
        name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name = 'account/registration/password_reset_confirm.html'), 
        name='password_reset_confirm'),
    path('password-reset-done/', auth_views.PasswordResetDoneView.as_view(
        template_name = "account/registration/password_reset_done.html"), 
        name='password_reset_done'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name = "account/registration/password_reset_complete.html"), 
        name='password_reset_complete'),
    ]