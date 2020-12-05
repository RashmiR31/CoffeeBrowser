from django.contrib import admin
from . models import Import,Export,Country,Types
# Register your models here.

@admin.register(Import)
class ImportAdmin(admin.ModelAdmin):
    #list_display = ['Country_ID','Type_ID','Total Charges']
    pass

@admin.register(Export)
class ExportAdmin(admin.ModelAdmin):
    #list_display = ['Country_ID','Type_ID','Total Charges']
    pass

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    #list_display = ['Country_ID','Type_ID','Total Charges']
    pass

@admin.register(Types)
class TypesAdmin(admin.ModelAdmin):
    #list_display = ['Country_ID','Type_ID','Total Charges']
    pass