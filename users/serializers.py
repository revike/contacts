from rest_framework import serializers
from django.contrib.auth.hashers import make_password

from users.models import User
from users.validators import validate_password


class RegisterSerializer(serializers.ModelSerializer):
    """Serializer for register user"""
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password')

    def validate(self, attrs):
        data = super().validate(attrs)
        if not validate_password(data['password']):
            raise serializers.ValidationError('Invalid password')
        data['password'] = make_password(data['password'])
        return data
