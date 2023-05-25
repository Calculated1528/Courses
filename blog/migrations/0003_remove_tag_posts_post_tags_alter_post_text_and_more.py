# Generated by Django 4.0.8 on 2023-05-24 05:25

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        ('blog', '0002_rename_posts_post_rename_post_comments_post_comment_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='posts',
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(),
        ),
        migrations.DeleteModel(
            name='Post_comment',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]