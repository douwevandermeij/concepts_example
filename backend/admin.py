from django.contrib import admin
from backend.models import UserExtension


class UserExtensionAdmin(admin.ModelAdmin):
    list_display = ['user', 'name']


admin.site.register(UserExtension, UserExtensionAdmin)
