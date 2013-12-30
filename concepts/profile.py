from django.utils.translation import gettext_lazy as _


class ProfileConcept(object):
    class Meta:
        proxy = True

    def nickname(self):
        """
        Representing the nickname of a profile
        """


class Meta:
    proxy = True
    verbose_name = _('Profile')


def register(klass, nickname):
    mapping = {
        'nickname': nickname,
    }
    from concepts import profile as module
    module.ProfileConcept = type('ProfileConcept', (klass,), {
        '__module__': __name__,
        'Meta': Meta,
        '__unicode__': lambda self: self.nickname,
    })
    for _property, _field in mapping.items():
        if not hasattr(module.ProfileConcept, _property):
            setattr(module.ProfileConcept, _property, property(
                lambda self: getattr(self, _field),
                lambda self, value: setattr(self, _field, value),
            ))
