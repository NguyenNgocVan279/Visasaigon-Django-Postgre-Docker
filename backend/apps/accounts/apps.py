from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.accounts'        # Đường dẫn Python thực tế đến app
    label = 'accounts'            # Tên app dùng cho AUTH_USER_MODEL, migrations
    verbose_name = 'Accounts'     # Tên hiển thị trong Django Admin
