from django.contrib import admin
from . models import Import,Export,Country,Types
# Register your models here.

@admin.register(Import)
class ImportAdmin(admin.ModelAdmin):
    list_display = ['country_id','type_id','I_total_charges']
    

@admin.register(Export)
class ExportAdmin(admin.ModelAdmin):
    list_display = ['country_id','type_id','E_total_charges']
    

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    pass

@admin.register(Types)
class TypesAdmin(admin.ModelAdmin):
    pass