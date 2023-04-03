from .base import *
import os
from google.oauth2 import service_account

SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = False

ALLOWED_HOSTS = ['coffee-shop-production-b9b3.up.railway.app', 'cafena.store', 'www.cafena.store']
CSRF_TRUSTED_ORIGINS = ['https://coffee-shop-production-b9b3.up.railway.app',  'https://cafena.store', 'https://www.cafena.store']

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True

DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ['PGDATABASE'],
        "USER": os.environ['PGUSER'],
        "PASSWORD": os.environ['PGPASSWORD'],
        "HOST": os.environ['PGHOST'],
        "PORT": os.environ['PGPORT']
    }
}

STATICFILES_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'

GS_BUCKET_NAME = os.environ['gs_bucket_name']
GS_CREDENTIALS = service_account.Credentials.from_service_account_info(
    {
        "type": os.environ["type"],
        "project_id": os.environ["project_id"],
        "private_key_id": os.environ["private_key_id"],
        "private_key": os.environ["private_key"],
        "client_email": os.environ["client_email"],
        "client_id": os.environ["client_id"],
        "auth_uri": os.environ["auth_uri"],
        "token_uri": os.environ["token_uri"],
        "auth_provider_x509_cert_url": os.environ["auth_provider_x509_cert_url"],
        "client_x509_cert_url": os.environ["client_x509_cert_url"],
    }
)
