from django.apps import AppConfig


class VisaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.visa'
    label = 'visa'
    verbose_name = 'Visa'     # Tên hiển thị trong Django Admin
