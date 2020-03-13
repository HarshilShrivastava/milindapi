from wholeseller.models import (
Wholeseller
)
from rest_framework import serializers

class WholesellerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Wholeseller
        fields=['Name']