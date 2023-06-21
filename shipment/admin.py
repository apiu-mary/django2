from django.contrib import admin
from .models import Shipment
class ShipmentAdmin(admin.ModelAdmin):
    list_display=("date", "order ","location","options","typeofdelivery","cost","time","status")
admin.site.register(Shipment)    


