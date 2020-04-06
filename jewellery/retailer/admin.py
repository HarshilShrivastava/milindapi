from django.contrib import admin
from retailer.models import (
    retailer,
    ROrnament,
    Rbucket,
    
)
admin.site.register(retailer)
admin.site.register(ROrnament)
# Register your models here.
admin.site.register(Rbucket)
