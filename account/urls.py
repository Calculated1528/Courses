from django.urls import path 
from django.contrib.auth import logout
from django.contrib.auth.views import logout_then_login
from . import views

app_name = 'user_login'
urlpatterns = [
    path('',views.user_login, name='login')
]

app_name = 'account'
urlpatterns = [
    path('logout-then-login/', views.logout_then_login, name='logout_then_login')
]