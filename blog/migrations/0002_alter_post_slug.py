# Generated by Django 4.0.8 on 2023-05-25 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True, unique=True, verbose_name='URL'),
        ),
    ]
