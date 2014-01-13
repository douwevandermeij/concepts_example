from django.contrib import admin
from webshop.models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_nr', 'customer']


admin.site.register(Order, OrderAdmin)
