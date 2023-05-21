# Generated by Django 4.0.8 on 2023-05-21 17:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_posts_post_rename_post_comments_post_comment_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0004_profile_delete_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, default='default.jpg', upload_to='media')),
                ('subscription', models.IntegerField(default=0)),
                ('followers', models.IntegerField(default=0)),
                ('user', models.OneToOneField(default=5, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('voted_posts', models.ManyToManyField(to='blog.post')),
            ],
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]