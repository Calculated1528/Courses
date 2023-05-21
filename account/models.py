from django.db import models
from django.contrib.auth.models import User
from blog.models import Post


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,default=5)
    photo = models.ImageField(null=True, blank=True, upload_to="media")
    voted_posts = models.ManyToManyField(Post)
    subscription = models.IntegerField(default=0)
    followers = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user.username}'