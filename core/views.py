from rest_framework import viewsets
from .serializers import CategorySerializer, ManufacturerSerializer, DeveragesSerializer
from .models import Category, Manufacturer, Deverages


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ManufacturerViewSet(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer

class DeveragesViewSet(viewsets.ModelViewSet):
    queryset = Deverages.objects.all()
    serializer_class = DeveragesSerializer