from django.urls import path 
from . import views
#from django.contrib.auth import views as dviews
#from django.contrib.auth import logout_then_login

app_name = 'account'
urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    #path('logout/', dviews.LogoutView.as_view(), name='logout'), /  2й вариант logout
]