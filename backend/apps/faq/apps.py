from django.apps import AppConfig


class FaqConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.faq'
    label = 'faq'
    verbose_name = 'Câu hỏi thường gặp'     # Tên hiển thị trong Django Admin
