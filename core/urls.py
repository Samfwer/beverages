from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ManufacturerViewSet,DeveragesViewSet

router = DefaultRouter()
router.register(r'Категория', CategoryViewSet)
router.register(r'Производители', ManufacturerViewSet)
router.register(r'Напитки', DeveragesViewSet)

urlpatterns = [
    path('', include(router.urls)),

]