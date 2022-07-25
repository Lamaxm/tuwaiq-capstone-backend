from rest_framework import serializers
from .models import Employee , Fav


class EmployeesSerializer(serializers.ModelSerializer):
    """For Serializing Comment"""
    class Meta :
        model = Employee
        fields = '__all__'

class FavSerializer(serializers.ModelSerializer):
    """For Serializing Comment"""
    class Meta :
        model = Fav
        fields = '__all__'