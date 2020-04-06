from django.db import models
from django.contrib.auth import (
    get_user_model,
)
User=get_user_model()
class retailer(models.Model):
    User=models.OneToOneField(User,  on_delete=models.CASCADE)
    Name=models.CharField( max_length=250)
# Create your models here.
class ROrnament(models.Model):
    retailer=models.ForeignKey(retailer, on_delete=models.CASCADE)
    Name=models.CharField( max_length=50)
    Type=models.CharField( max_length=50)

class Rbucket(models.Model):
    FROM=models.ForeignKey(retailer, on_delete=models.CASCADE)
    ORNAMENT=models.ForeignKey(ROrnament, on_delete=models.CASCADE)




