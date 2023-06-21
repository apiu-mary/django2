from django.db import models

# Create your models here.
class Vendor(models.Model):
    name = models.CharField(max_length=32)
    contact = models.BigIntegerField()
    email = models.CharField(max_length=32)
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    def __strrr__(self):
        return self.name
