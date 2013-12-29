from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from frontend.models import ProfileInfo


class ProfileInfoAdmin(admin.ModelAdmin):
    class Meta:
        plural_name = _('Profile\'s info')
    list_display = ['profile']


admin.site.register(ProfileInfo, ProfileInfoAdmin)
