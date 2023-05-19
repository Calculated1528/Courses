from django.db import models

# Create your models here.

"""
class Users(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    passord = models.CharField(max_length=20)
    reg_time = models.DateTimeField()
    photo = models.ImageField(upload_to='photos/')

class Roles(models.Model):
    name = models.Model(max_length=30); 

class UsersRoles(models.Model):
  user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
  role_id = models.ForeignKey(Roles, on_delete=models.CASCADE)

class Privilege(models.Model):
    name = models.CharField(max_length=30)
    delete_your_posts = models.BooleanField
    edit_your_posts = models.BooleanField
    delete_your_post_comments = models.BooleanField
    edit_your_post_comments = models.BooleanField
    edit_your_tag2posts = models.BooleanField
    delete_other_posts = models.BooleanField
    edit_other_posts = models.BooleanField
    delete_other_post_comments = models.BooleanField
    edit_other_post_comments = models.BooleanField
    edit_other_tag2posts = models.BooleanField; 

class Posts(models.Model):  
    moderation_status = models.BooleanField
    text = models.CharField(max_length=max)
    time = models.IntegerField
    title = models.CharField(max_length=50)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    view_count = models.IntegerField()
    created_date = models.DateTimeField()
    published_date = models.DateTimeField(); 

class Tags(models.Model):
    name = models.CharField(max_length=30); 

class Post_comments(models.Model):
    id = models.ForeignKey(Posts, on_delete=models.CASCADE)
    post_id = models.IntegerField
    text = models.TextField()
    user_id = models.IntegerField; 

class post_votes(models.Model):
    post_votes_id = models.ForeignKey(Posts, on_delete=models.CASCADE)
    post_id = models.IntegerField()
    time = models.IntegerField()
    user_id = models.IntegerField()
    value = models.IntegerField(); 

class Tag2posts(models.Model):
    post_id = models.ForeignKey(Posts, on_delete=models.CASCADE)
    tag_id = models.ForeignKey(Tags, on_delete=models.CASCADE)'

"""