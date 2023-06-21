from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField()
    image = models.ImageField()
    price = models.DecimalField(max_digits=6,decimal_places=2)
    stock =models.PositiveBigIntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    
# whenever  you are creating an object always create an string representation of it
# columns=attributes 
# table=object
# rows=instances
# pillow is a library for installing images
