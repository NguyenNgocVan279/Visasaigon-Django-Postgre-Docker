from django.contrib import admin
from .models import Country, VisaType, RequiredDocument

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'region', 'created_at')
    search_fields = ('name', 'code', 'region')

@admin.register(VisaType)
class VisaTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'purpose', 'created_at')
    list_filter = ('country', 'purpose')
    search_fields = ('name', 'country__name')

@admin.register(RequiredDocument)
class RequiredDocumentAdmin(admin.ModelAdmin):
    list_display = ('name', 'visa_type', 'country', 'created_at')
    list_filter = ('visa_type', 'country')
    search_fields = ('name', 'visa_type__name', 'country__name')
