from tastypie.resources import ModelResource
from shop.models import Category, Course
from django.contrib.auth.models import User
# from blog.models import Post, Post_comment
# from tastypie.authorization import Authorization
# from .authentication import CustomAuthentication
# # from blog.models import Post, Post_comment

# # Create your models here.
# class CategoryResource(ModelResource):
#     class Meta:
#         queryset = Category.objects.all()
#         resource_name = 'categories'
#         allowed_metods = ['get']

# class CourseResource(ModelResource):
#     class Meta:
#         queryset = Course.objects.all()
#         resource_name = 'courses'
#         allowed_metods = ['get', 'delete', 'post']
#         authentication = CustomAuthentication()
#         authorization = Authorization()

    # def hydrate(self, bundle):
    #     bundle.obj.category_id = bundle.data['category_id']
    #     return bundle
    
    # def dehydrate(self, bundle):
    #     bundle.data['category_id'] = bundle.obj.category
    #     return bundle
    
    # def dehydrate_title(self, bundle):
    #     return bundle.data['title'].upper()


    
class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'users'
        allowed_metods = ['get']

# class PostResource(ModelResource):
#     class Meta:
#         queryset = Post.objects.all()
#         resource_name = 'posts'
#         allowed_metods = ['get', 'post', 'delete']
#         authentication = CustomAuthentication()
#         authorization = Authorization()


# class Post_commentResource(ModelResource):
#     class Meta:
#         queryset = Post_comment.objects.all()
#         resource_name = 'post_comments'
#         allowed_metods = ['get', 'post', 'delete']
#         authentication = CustomAuthentication()
#         authorization = Authorization()