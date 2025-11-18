from django.contrib import admin
from .models import FAQCategory, FAQItem

@admin.register(FAQCategory)
class FAQCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)

@admin.register(FAQItem)
class FAQItemAdmin(admin.ModelAdmin):
    list_display = ('question', 'category', 'order', 'created_at')
    list_filter = ('category',)
    search_fields = ('question', 'answer')
