from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy


app_name = 'account'
urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('change_password/',  auth_views.PasswordChangeView.as_view(templated_name='account/registration/change_password.html', success_url=reverse_lazy('account:change_password_done')), name='change_password'),
    path('change_password-done/', auth_views.PasswordChangeDoneView.as_view(template_name='account/registration/change_password_done.html'), name='change_password_done'),
]
