# Generated by Django 4.0.8 on 2023-05-20 19:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='user',
        ),
        migrations.RemoveField(
            model_name='tag2posts',
            name='post',
        ),
        migrations.RemoveField(
            model_name='tag2posts',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='userinfo',
            name='followers',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='photo',
            field=models.ImageField(default='default.jpg', upload_to='user_photo'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='subscription',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='user',
            field=models.OneToOneField(default=5, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='voted_posts',
            field=models.ManyToManyField(to='blog.posts'),
        ),
        migrations.DeleteModel(
            name='Post_comments',
        ),
        migrations.DeleteModel(
            name='Posts',
        ),
        migrations.DeleteModel(
            name='Tag2posts',
        ),
        migrations.DeleteModel(
            name='Tags',
        ),
    ]