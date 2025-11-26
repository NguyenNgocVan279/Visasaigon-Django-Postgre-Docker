from django.contrib import admin
from .models import Country, VisaType, RequiredDocument, CountryDetail, CountrySection, CountryTip

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'cover_image', 'flag_image', 'code', 'region')
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


# ---------------------------
# Bổ sung các model mới
# ---------------------------
@admin.register(CountryDetail)
class CountryDetailAdmin(admin.ModelAdmin):
    list_display = ('country', 'hero_title', 'overview_title', 'created_at')
    search_fields = ('country__name', 'hero_title', 'overview_title')

@admin.register(CountrySection)
class CountrySectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'country', 'order', 'image', 'image_left', 'created_at')
    list_filter = ('country',)
    search_fields = ('title', 'country__name')
    ordering = ('country', 'order')

@admin.register(CountryTip)
class CountryTipAdmin(admin.ModelAdmin):
    list_display = ('country', 'tip_type', 'content', 'order', 'created_at')
    list_filter = ('country', 'tip_type')
    search_fields = ('content', 'country__name')
    ordering = ('country', 'order')