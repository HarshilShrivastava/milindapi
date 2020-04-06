from retailer.models import (
    retailer,
    ROrnament,
    Rbucket
)
from wholeseller.models import (
WRI

)
from rest_framework import serializers

class retailerserializer(serializers.ModelSerializer):
    class Meta:
        model=retailer
        fields=['Name']

class ROrnamentserializer(serializers.ModelSerializer):
    class Meta:
        model=ROrnament
        fields=['Name','Type']
    
class BucketSerializer(serializers.ModelSerializer):
    x=serializers.SerializerMethodField('get_name')
    y=serializers.SerializerMethodField('get_type')
    
    class Meta:
        model=Rbucket
        fields=['ORNAMENT','x','y']
    def get_name(self,o):
        a=o.ORNAMENT.Name
        return a
    def get_type(self,o):
        a=o.ORNAMENT.Type
        return a    


class WholesellerRetailerrequestserializer(serializers.ModelSerializer):
    class Meta:
        model=WRI
        fields='__all__'