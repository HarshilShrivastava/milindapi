from manufacturer.models import(
    Manufacturer,
    MOrnament,
    Mbucket,
    MWIR
)
from rest_framework import serializers
class manufacturerserializer(serializers.ModelSerializer):
    class Meta:
        model=Manufacturer
        fields=['Name']


class MOrnamentserializer(serializers.ModelSerializer):
    class Meta:
        model=MOrnament
        fields=['Name','Type']

class MbucketSerializer(serializers.ModelSerializer):
    x=serializers.SerializerMethodField('get_name')
    y=serializers.SerializerMethodField('get_type')
    
    class Meta:
        model=Mbucket
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