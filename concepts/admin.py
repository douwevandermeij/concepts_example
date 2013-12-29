from django.contrib import admin
from concepts.models import ProfileConcept


class ProfileConceptAdmin(admin.ModelAdmin):
    list_display = ['nickname']


admin.site.register(ProfileConcept, ProfileConceptAdmin)
