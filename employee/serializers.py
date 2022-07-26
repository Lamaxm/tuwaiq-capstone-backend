from rest_framework import serializers
from .models import Employee , Fav , ReqEmployee


class EmployeesSerializer(serializers.ModelSerializer):
    """For Serializing Employees"""
    class Meta :
        model = Employee
        fields = '__all__'

class FavSerializer(serializers.ModelSerializer):
    """For Serializing Fav"""
    class Meta :
        model = Fav
        fields = '__all__'

class ReqEmployeeSerializer(serializers.ModelSerializer):
    """For Serializing Requests"""
    class Meta :
        model = ReqEmployee
        fields = '__all__'