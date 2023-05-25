from django.urls import path 
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<slug:slug>/', views.single_post, name='single_post'),
    path('tagged/', views.tagged, name='tagged')
]