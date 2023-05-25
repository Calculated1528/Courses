from django.urls import path, include
from tastypie.api import Api
from api.models import UserResource 
# Post_commentResource, PostResource
# from api.models import CategoryResource, CourseResource
api = Api(api_name='v1')
api.register(UserResource())
# api.register(PostResource())
# api.register(Post_commentResource())

# api.register(CourseResource())
# api.register(CategoryResource())
urlpatterns = [
    path('', include(api.urls), name='index'),
    path('', include(api.urls), name='courses')
]
