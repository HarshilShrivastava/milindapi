from wholeseller.models import (
Wholeseller,
WOrnament,
Wbucket,
WRI

)

from manufacturer.models import(
MWIR
)
from rest_framework import serializers

class WholesellerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Wholeseller
        fields=['Name']


class WholesellerOrnamentSerializer(serializers.ModelSerializer):
    class Meta:
        model=WOrnament
        fields=['Name','Type']


class WbucketSerializer(serializers.ModelSerializer):
    x=serializers.SerializerMethodField('get_name')
    y=serializers.SerializerMethodField('get_type')
    
    class Meta:
        model=Wbucket
        fields=['ORNAMENT','x','y']
    def get_name(self,o):
        a=o.ORNAMENT.Name
        return a
    def get_type(self,o):
        a=o.ORNAMENT.Type
        return a    

class RequestListSerializer(serializers.ModelSerializer):
    class Meta:
        model=MWIR
        fields='__all__'

class WholesellerRetailerrequestserializer(serializers.ModelSerializer):
    class Meta:
        model=WRI
        fields='__all__'