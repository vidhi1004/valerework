from django.contrib import admin
from .models import Customer
# Register your models here.


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name',
                    'email', 'phone_number', 'gender', 'date_of_birth']


admin.site.register(Customer, CustomerAdmin)
