from django.db import models

# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=14)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)

    def register(self):
        self.save()

    # check if user exists
    def isExists(self):
        if Customer.objects.filter(email = self.email):
            return True
        return False