from .base import *
import os

DEBUG = False

# -----------------------------------------------------------------------------
# SECRET KEY & HOSTS
# -----------------------------------------------------------------------------
SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]

ALLOWED_HOSTS = [
    host.strip() for host in os.environ.get("ALLOWED_HOSTS", "").split(",")
    if host.strip()
] or ["localhost"]

# CSRF Trusted Origins (bắt buộc)
CSRF_TRUSTED_ORIGINS = [
    "https://visasaigon.net",
    "https://www.visasaigon.net",
]

STATICFILES_DIRS = []  # production không dùng STATICFILES_DIRS

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
# STATIC & MEDIA - served by Nginx
# -----------------------------------------------------------------------------
STATIC_URL = "/static/"
MEDIA_URL = "/media/"

STATIC_ROOT = "/vol/static"
MEDIA_ROOT = "/vol/media"

# -----------------------------------------------------------------------------
# SECURITY HARDENING
# -----------------------------------------------------------------------------
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# HSTS – chỉ bật khi đã chạy HTTPS ổn định
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# -----------------------------------------------------------------------------
# LOGGING - Docker friendly
# -----------------------------------------------------------------------------
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,

    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },

    "root": {
        "handlers": ["console"],
        "level": "INFO",
    },
}
