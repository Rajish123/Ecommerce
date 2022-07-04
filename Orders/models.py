from django.db import models
from Store.models import Product
from Accounts.models import Customer
from datetime import datetime

# Create your models here.
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=50, default='',blank=True)
    phone= models.CharField(max_length=50, default='',blank=True)
    date = models.DateField(default=datetime.today)