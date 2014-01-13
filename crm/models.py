from django.db import models


class Customer(models.Model):
    account_nr = models.IntegerField()
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name
