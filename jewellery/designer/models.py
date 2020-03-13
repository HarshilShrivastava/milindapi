from django.db import models
from django.contrib.auth import (
    get_user_model,
)
User=get_user_model()
# Create your models here.
class designer(models.Model):
    User=models.OneToOneField(User, on_delete=models.CASCADE)
    Name=models.CharField( max_length=250)