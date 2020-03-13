from manufacturer.models import(
    Manufacturer
)
from rest_framework import serializers
class manufacturerserializer(serializers.ModelSerializer):
    class Meta:
        model=Manufacturer
        fields=['Name']