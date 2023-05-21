from django.contrib import admin
from .models import UserInfo

admin.site.site_header = "Admin"
admin.site.site_title = "UserInfo"
admin.site.index_title = "Welcome to the Admin area"

class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('user','subscription','followers')

admin.site.register(UserInfo, UserInfoAdmin)
