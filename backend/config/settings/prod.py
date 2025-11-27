from .base import *
import os

DEBUG = False

# -----------------------------------------------------------------------------
# SECRET KEY & HOSTS
# -----------------------------------------------------------------------------
SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]  # bắt buộc có trong .env.prod

# ALLOWED_HOSTS từ biến môi trường (phân tách dấu phẩy)
ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS", "").split(",")
# Loại bỏ chuỗi rỗng (trường hợp env rỗng)
ALLOWED_HOSTS = [host.strip() for host in ALLOWED_HOSTS if host.strip()] or ["localhost"]

# IMPORTANT
STATICFILES_DIRS = []  # disable STATICFILES_DIRS for production


# -----------------------------------------------------------------------------
# DATABASE - PostgreSQL
# -----------------------------------------------------------------------------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("POSTGRES_DB"),
        "USER": os.environ.get("POSTGRES_USER"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
        "HOST": os.environ.get("POSTGRES_HOST"),
        "PORT": os.environ.get("POSTGRES_PORT", "5432"),
    }
}


# -----------------------------------------------------------------------------
# STATIC & MEDIA (phục vụ bởi Nginx)
# -----------------------------------------------------------------------------
STATIC_URL = "/static/"
MEDIA_URL = "/media/"

STATIC_ROOT = os.path.join(BASE_DIR, "static")  # nơi collectstatic
MEDIA_ROOT = os.path.join(BASE_DIR, "media")    # lưu uploads


# -----------------------------------------------------------------------------
# SECURITY HARDENING
# -----------------------------------------------------------------------------
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

# Cookie HTTPS (Nginx giữ SSL, Gunicorn nhận HTTP)
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Django biết request gốc là HTTPS
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")


# -----------------------------------------------------------------------------
# LOGGING PRODUCTION
# -----------------------------------------------------------------------------
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,

    "formatters": {
        "verbose": {
            "format": "[{levelname}] {asctime} {name} — {message}",
            "style": "{",
        },
    },

    "handlers": {
        "file": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "filename": os.path.join(BASE_DIR, "logs", "django.log"),
            "formatter": "verbose",
        },
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },

    "root": {
        "handlers": ["file", "console"],
        "level": "INFO",
    },
}
