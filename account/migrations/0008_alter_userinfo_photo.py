# Generated by Django 4.0.8 on 2023-05-22 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_rename_userfk_userinfo_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='photo',
            field=models.ImageField(default='default.jpg', upload_to='account/static'),
        ),
    ]