from designer.models import (
    designer
)
from rest_framework import serializers
class designerserializer(serializers.ModelSerializer):
    class Meta:
        model=designer
        fields=['Name']