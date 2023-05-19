from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class UserInfo(models.Model):
    phone_number = models.PhoneNumberField()
    photo = models.ImageField(upload_to='photos/')

# class Roles(models.Model):
#     name = models.Model(max_length=30); 

# class UsersRoles(models.Model):
#   user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
#   role_id = models.ForeignKey(Roles, on_delete=models.CASCADE)

class Posts(models.Model):  
    moderation_status = models.BooleanField
    text = models.CharField(max_length=max)
    time = models.DateField()
    title = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    view_count = models.IntegerField()
    created_date = models.DateField(default=timezone.now)
    published_date = models.DateField()

class Tags(models.Model):
    name = models.CharField(max_length=30); 

class Post_comments(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    text = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

"""
"class post_votes(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    post_id = models.IntegerField()
    time = models.DateField()
    user_id = models.IntegerField()
    value = models.IntegerField(); 
""""
class Tag2posts(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tags, on_delete=models.CASCADE)
