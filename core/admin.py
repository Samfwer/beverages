from django.contrib import admin
from .models import Category,Manufacturer,Deverages

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    search_fields = ('name',)
    list_filter = ('name',)
    save_on_top = False
    save_as = True

@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Deverages)
class DeveragesAdmin(admin.ModelAdmin):
    list_display = ['id','name','category','manufacturer']

# @admin.register(Price)
# class PriceAdmin(admin.ModelAdmin):
#     list_display = ['id','name']
