from django.urls import path 
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:post_id>', views.single_post, name='single_post'),
    path('home/', views.home_view, name='home_view'),
    path('detail/', views.detail_view, name='detail'),
    path('tagged/', views.tagged, name='tagged')
]