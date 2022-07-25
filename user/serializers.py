from rest_framework import serializers
from .models import employee ,fav


class favSerializer(serializers.ModelSerializer):
    """For Serializing Comment"""
    class Meta :
        model = fav
        fields = '__all__'

