# Generated by Django 4.0.8 on 2023-06-09 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0001_initial'),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='voted_posts',
            field=models.ManyToManyField(to='blog.post'),
        ),
    ]
