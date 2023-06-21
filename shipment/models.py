from django.db import models

# Create your models here.

class Shipment(models.Model):
    date_ordered = models.DateTimeField(auto_now=True)
    date_delivered =models.DateTimeField(auto_now=True)
    order = models.CharField(max_length=32)
    location = models.CharField(max_length=32)
    options = models.CharField(max_length=32)
    typeofdelivery = models.CharField(max_length=32)
    cost = models.DecimalField(max_digits=6,decimal_places=2)
    status = models.CharField(max_length=32)
def __strr__(self):
    return self.location
