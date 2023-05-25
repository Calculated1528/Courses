from django.contrib import admin
from .models import Post
# ,Tag,Post_comment
import random
# Register your models here.

admin.site.site_header = "Blog Admin"
admin.site.site_title = "Blogs"
admin.site.index_title = "Welcome to the Admin area"

class PostsAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'views_count','comments_count', 'post_rating')
    prepopulated_fields = {"slug": ("title",)}

# class Post_commentsAdmin(admin.ModelAdmin):
#     list_display = ('post', 'text', 'user')


admin.site.register(Post, PostsAdmin)

# admin.site.register(Post_comment, Post_commentsAdmin)

