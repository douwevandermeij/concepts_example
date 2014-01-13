from django.db import models


class Order(models.Model):
    customer = models.ForeignKey('concepts.CustomerConcept')
    order_nr = models.IntegerField()
