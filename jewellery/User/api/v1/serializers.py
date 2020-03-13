from rest_framework import serializers
from User.models import user
class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta():
        model = user
        fields = ['email', 'username', 'password', 'confirm_password', 'IS_MANUFACTURER','IS_DESIGNER','IS_WHOLESELLER','IS_RETAILER','IS_CITIZEN']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        user1 = user(
            email = self.validated_data['email'].lower(),
            username = self.validated_data['username'].lower(),
            IS_MANUFACTURER=self.validated_data['IS_MANUFACTURER'],
            IS_DESIGNER=self.validated_data['IS_DESIGNER'],
            IS_WHOLESELLER=self.validated_data['IS_WHOLESELLER'],
            IS_RETAILER=self.validated_data['IS_RETAILER'],
            IS_CITIZEN=self.validated_data['IS_CITIZEN']
        )
        password = self.validated_data['password']
        confirm_password = self.validated_data['confirm_password']

        if password != confirm_password:
            raise serializers.ValidationError({'password': 'Password must match.'})
        user1.set_password(password)
        user1.save()
        return user1

class UserLoginSerializers(serializers.Serializer):
    username=serializers.CharField(max_length=255)
    password=serializers.CharField(max_length=255)
    class Meta:
        fields=['username','password']

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    confirm_new_password = serializers.CharField(required=True)