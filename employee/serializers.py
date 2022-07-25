from rest_framework import serializers
from .models import User, profile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'password']

class profileSerializer(serializers.ModelSerializer):
    class Meta:
        model = profile
        fields = '__all__'