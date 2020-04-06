from django.db import models
from django.contrib.auth import (
    get_user_model,
)
from wholeseller.models import(
    Wholeseller
)
from django.utils import timezone
User=get_user_model()
# Create your models here.
class Manufacturer(models.Model):
    User=models.OneToOneField(User, on_delete=models.CASCADE)
    Name=models.CharField( max_length=250)

class MOrnament(models.Model):
    Manufacturer=models.ForeignKey(Manufacturer,on_delete=models.CASCADE)
    Name=models.CharField( max_length=50)
    Type=models.CharField( max_length=50)


class Mbucket(models.Model):
    FROM=models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    ORNAMENT=models.ForeignKey(MOrnament, on_delete=models.CASCADE)

class MWIR(models.Model):

    Manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
        related_name="ManufacturerR",
    )
    Wholeseller = models.ForeignKey(
        Wholeseller,
        on_delete=models.CASCADE,
        related_name="WholesellerR",
    )
    message = models.TextField( blank=True)
    created = models.DateTimeField(default=timezone.now)
    rejected = models.DateTimeField(blank=True, null=True)
    viewed = models.DateTimeField(blank=True, null=True)

class MWIC(models.Model):
    Manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
        related_name="ManufacturerC",
    )
    Wholeseller = models.ForeignKey(
        Wholeseller,
        on_delete=models.CASCADE,
        related_name="WholesellerC",
    )
    created = models.DateTimeField(default=timezone.now)
    
