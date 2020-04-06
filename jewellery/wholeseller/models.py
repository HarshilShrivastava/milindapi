from django.db import models
from retailer.models import(
    retailer
)
from django.contrib.auth import (
    get_user_model,
)
from django.utils import timezone
User=get_user_model()
class Wholeseller(models.Model):
    User=models.OneToOneField(User, on_delete=models.CASCADE)
    Name=models.CharField( max_length=250)

class WOrnament(models.Model):
    Wholeseller=models.ForeignKey( Wholeseller, on_delete=models.CASCADE)
    Name=models.CharField( max_length=50)
    Type=models.CharField( max_length=50)

class Wbucket(models.Model):
    FROM=models.ForeignKey(Wholeseller, on_delete=models.CASCADE)
    ORNAMENT=models.ForeignKey(WOrnament, on_delete=models.CASCADE)

class WRI(models.Model):

    retailer = models.ForeignKey(
        retailer,
        on_delete=models.CASCADE,
        related_name="retailer",
    )
    Wholeseller1 = models.ForeignKey(
        Wholeseller,
        on_delete=models.CASCADE,
        related_name="Wholeseller1",
    )

    message = models.TextField( blank=True)

    created = models.DateTimeField(default=timezone.now)
    rejected = models.DateTimeField(blank=True, null=True)
    viewed = models.DateTimeField(blank=True, null=True)

class WRIC(models.Model):
    retailer = models.ForeignKey(
        retailer,
        on_delete=models.CASCADE,
        related_name="retailerC",
    )
    Wholeseller1 = models.ForeignKey(
        Wholeseller,
        on_delete=models.CASCADE,
        related_name="Wholeseller1C",
    )