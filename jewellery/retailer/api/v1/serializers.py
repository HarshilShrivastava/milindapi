from retailer.models import (
    retailer
)
from rest_framework import serializers

class retailerserializer(serializers.ModelSerializer):
    class Meta:
        model=retailer
        fields=['Name']