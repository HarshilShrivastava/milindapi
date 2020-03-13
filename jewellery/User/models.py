from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class user(AbstractUser):
    IS_MANUFACTURER=models.BooleanField(null=True)
    IS_DESIGNER=models.BooleanField(null=True)
    IS_WHOLESELLER=models.BooleanField(null=True)
    IS_RETAILER=models.BooleanField(null=True)
    IS_CITIZEN=models.BooleanField(null=True)


    


    