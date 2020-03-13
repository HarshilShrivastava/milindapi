from citizen.models import (
    Citizen
)
from rest_framework import serializers
class Citizenserializer(serializers.ModelSerializer):
    class Meta:
        model=Citizen
        fields=['Name']