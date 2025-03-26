from rest_framework import serializers
from . import models

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        models = models.Address
        fields = '__all__'

class ExtrasSerializer(serializers.ModelSerializer):
    class Meta:
        models = models.Extras
        fields = '__all__'