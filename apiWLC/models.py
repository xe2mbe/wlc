from django.db import models
from django.db.models.fields import IPAddressField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import IntegerField, Model

# Create your models here.

class ap(models.Model):
    model = models.CharField(max_length=100)
    IP = models.GenericIPAddressField()
    ap_name = models.CharField(max_length=10)
    
    class Meta:
        ordering = ['ap_name'] 

class guestuser(Model):
    netuser = models.CharField(max_length=40)
    netpass = models.CharField(max_length=40)
    wlanID = models.IntegerField(
        default= 4,
        validators = [
            MinValueValidator(1),
            MaxValueValidator(4)
            ]
        )
    lifetime = models.IntegerField(
        default= 28800,
        validators = [
            MinValueValidator(0),
            MaxValueValidator(2592000)
            ]
        )
    description = models.CharField(max_length=40)
    aps = models.ForeignKey(ap, on_delete=models.DO_NOTHING)        
         
    class Meta:
        ordering = ['id']   