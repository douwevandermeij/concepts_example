from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _
from concepts import profile


class UserExtension(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(_('Name'), max_length=255, null=True, blank=True)


profile.register(UserExtension, nickname='name')
