from .base import *
import os

# Bật debug dev
DEBUG = True
ALLOWED_HOSTS = ["*"]

# Secret dev local
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "dev-secret-key")

# Database (lấy từ env hoặc dùng sqlite cho dev)
if os.environ.get("DATABASE_URL"):
    import dj_database_url
    DATABASES = {"default": dj_database_url.parse(os.environ.get("DATABASE_URL"))}
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.environ.get("POSTGRES_DB", "myproject_db"),
            "USER": os.environ.get("POSTGRES_USER", "myproject_user"),
            "PASSWORD": os.environ.get("POSTGRES_PASSWORD", "myproject_pass"),
            "HOST": os.environ.get("POSTGRES_HOST", "db"),
            "PORT": os.environ.get("POSTGRES_PORT", "5432"),
        }
    }

# Logging dev
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {"console": {"class": "logging.StreamHandler"}},
    "root": {"handlers": ["console"], "level": "DEBUG"},
}
