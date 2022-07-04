import dataclasses
from django.contrib import admin
from .models import Order

# Register your models here.
@admin.register(Order)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product','customer','quantity','price','address','phone','date',)

