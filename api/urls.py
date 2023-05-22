from django.urls import path, include
from api.models import CategoryResource, CourseResource
from tastypie.api import Api
from api.models import UserResource

api = Api(api_name='v1')
# api.register(CourseResource())
# api.register(CategoryResource())
api.register(UserResource())
urlpatterns = [
    path('', include(api.urls), name='index'),
    path('', include(api.urls), name='courses')
]
