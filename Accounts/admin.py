from django.contrib import admin
from Accounts.models import *

# Register your models here.

@admin.register(Customer)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','phone','email','password')

