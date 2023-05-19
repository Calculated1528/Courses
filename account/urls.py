from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path('', views.account, name='index'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('registration/',  views.registration, name='registration'),
    path('change-password/',  views.change_password, name='change_password'),
]
