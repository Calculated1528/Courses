from django.urls import path 
from django.contrib.auth import logout
from django.contrib.auth.views import logout_then_login
from . import views

app_name = 'account'
urlpatterns = [
    path('login/',views.user_login, name='login'),
    path('logout/',views.user_logout, name='logout')
]
