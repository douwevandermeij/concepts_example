from django.conf import settings
from django.utils.translation import gettext_lazy as _
from concepts.util import load_class


class ProfileConcept(object):
    mapping = {}

    @property
    def nickname(self):
        return getattr(self, self.mapping['nickname'])

    @nickname.setter
    def nickname(self, value):
        setattr(self, self.mapping['nickname'], value)

    def __unicode__(self):
        return self.nickname


class Meta:
    proxy = True
    verbose_name = _('Profile')

# Set the producer at runtime
producer, mapping = settings.CONCEPTS['ProfileConcept']
attrs = {
    '__module__': __name__,
    'Meta': Meta,
    'mapping': mapping,
}
ProfileConcept = type('ProfileConcept', (load_class(producer), ProfileConcept,), attrs)
