from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



class Post(models.Model):  
    moderation_complete = models.BooleanField(default=False)
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=5000)
    user = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=5)
    views_count = models.IntegerField(default=0)
    comments_count = models.IntegerField(default=0)
    created_at = models.DateField(default=timezone.now)
    post_rating = models.IntegerField(default=0)


    def __str__(self):
        return f'{self.title}'

class Tag(models.Model):
    name = models.CharField(max_length=30)
    posts = models.ManyToManyField(Post)

    def __str__(self):
        return f'{self.name}'

class Post_comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=5)
    created_at = models.DateField(default=timezone.now)

    def __str__(self):
        return f'{self.text}'