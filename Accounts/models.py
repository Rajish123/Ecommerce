from django.db import models

# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    password = models.CharField(max_length=20)
