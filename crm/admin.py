from django.contrib import admin
from crm.models import Customer


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['account_nr', 'name']


admin.site.register(Customer, CustomerAdmin)
