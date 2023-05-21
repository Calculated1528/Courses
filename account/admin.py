from django.contrib import admin
from .models import Profile

admin.site.site_header = "Admin"
admin.site.site_title = "Profile"
admin.site.index_title = "Welcome to the Admin area"

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','subscription','followers')

admin.site.register(Profile, ProfileAdmin)
