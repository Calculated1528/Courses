from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy


app_name = 'account'
urlpatterns = [
    path('', views.account, name='index'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('registration/',  views.registration, name='registration'),
    path('change_password', views.change_password, name='change_password'),

    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name = "account/registration/password_reset.html", 
        email_template_name = "account/registration/password_reset_email.html"), name ='password_reset'),
    path
        ('^password-reset/done/$', auth_views.PasswordResetDoneView.as_view(template_name = "account/registration/password_reset_done.html"), 
         name ='password_reset_done'),
    path
        ('^password_reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$', auth_views.PasswordResetConfirmView.as_view(template_name = "account/registration/password_reset_confirm.html",
         success_url=reverse_lazy('account:password_reset_done')), name ='password_reset_confirm'),
    path
        ('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name = "account/registration/password_reset_complete.html"), 
         name ='password_reset_complete'),
         ]
#