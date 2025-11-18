from django.apps import AppConfig


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.blog'
    label = 'blog'
    verbose_name = 'Bài viết'     # Tên hiển thị trong Django Admin
