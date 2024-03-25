from rest_framework import serializers
from .models import Category, Manufacturer, Deverages


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ['name']

class DeveragesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deverages
        fields = '__all__'