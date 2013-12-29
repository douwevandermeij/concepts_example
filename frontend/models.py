from django.db import models
from django.utils.translation import gettext_lazy as _
from concepts.models import ProfileConcept


class ProfileInfo(models.Model):
    profile = models.OneToOneField(ProfileConcept)
    info = models.TextField(_('Info'), null=True, blank=True)
