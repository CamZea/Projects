from .models import User
from rest_framework.serializers import ModelSerializer, Serializer, EmailField, CharField
from django.contrib.auth.hashers import make_password


class UserLoginSerializer(Serializer):
    email= EmailField(required=True)
    password= CharField(required=True)

class UserSerializer(ModelSerializer):
    class Meta:
        model= User
        fields= '__all__'

    def create(self, validated_data):
        if 'password' in validated_data:
            validated_data['password']= make_password(
                validated_data['password']
            )
        return super().create(validated_data)


