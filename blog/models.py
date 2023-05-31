from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
import random,string


class Post(models.Model):
    moderation_complete = models.BooleanField(default=False)
    title = models.CharField(max_length=100)
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=5)
    views_count = models.IntegerField(default=0)
    comments_count = models.IntegerField(default=0)
    created_at = models.DateField(default=timezone.now)
    post_rating = models.IntegerField(default=0)
    tags = TaggableManager()
    slug = models.SlugField(unique=True, db_index=True, verbose_name="URL", null=True,blank=True, max_length=100)

    def str(self):
        return f'{self.title}'
    
    def save(self, *args, **kwargs):
        self.slug = slugify(''.join(random.choices(string.ascii_uppercase + string.digits, k=12)))
        super().save(*args, **kwargs)


# class Post_comment(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     text = models.TextField()
#     user = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=5)
#     created_at = models.DateField(default=timezone.now)

#     def __str__(self):
#         return f'{self.text}'