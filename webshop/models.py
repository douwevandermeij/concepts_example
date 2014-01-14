from django.db import models
from concepts.models import CustomerConcept


class Order(models.Model):
    customer = models.ForeignKey(CustomerConcept)
    order_nr = models.IntegerField()
