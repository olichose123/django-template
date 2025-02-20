from .base import *  # noqa: F403, F401
import os
from corsheaders.defaults import default_headers

DEBUG = os.environ.get("DJANGO_DEBUG", "False") == "True"
ALLOWED_HOSTS = ["*"]

# CSRF
CSRF_COOKIE_SAMESITE = "None"
CSRF_COOKIE_SECURE = True
CSRF_TRUSTED_ORIGINS = ["*"]

# CORS
CORS_ORIGIN_ALLOW_ALL = True
# CORS_ALLOWED_ORIGINS = ["https://example.com"]
# CORS_ALLOW_CREDENTIALS = True
CORS_PREFLIGHT_MAX_AGE = 0  # remove or set higher for production
CORS_ALLOW_HEADERS = (*default_headers,)

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.environ.get("POSTGRES_DB"),
        "USER": os.environ.get("POSTGRES_USER"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
        "HOST": os.environ.get("DB_HOST"),
        "PORT": os.environ.get("DB_PORT", "5432"),
    },
}

# Storage, static and media
STATIC_URL = "/static/"
STATIC_ROOT = "/usr/src/static/"
MEDIA_URL = "/media/"
MEDIA_ROOT = "/usr/src/media/"

# REST_FRAMEWORK configuration
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}
