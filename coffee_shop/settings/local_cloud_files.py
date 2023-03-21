from .base import *
import os
import json
from google.oauth2 import service_account

with open('credentials.json', 'r') as file:
    CREDENTIALS = json.loads(file.read())


SECRET_KEY = CREDENTIALS['SECRET_KEY']

DEBUG = True
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": CREDENTIALS['PGDATABASE'],
        "USER": CREDENTIALS['PGUSER'],
        "PASSWORD": CREDENTIALS['PGPASSWORD'],
        "HOST": CREDENTIALS['PGHOST'],
        "PORT": CREDENTIALS['PGPORT']
    }
}


STATICFILES_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'

GS_BUCKET_NAME = CREDENTIALS['gs_bucket_name']
GS_CREDENTIALS = service_account.Credentials.from_service_account_info(
    {
        "type": CREDENTIALS["type"],
        "project_id": CREDENTIALS["project_id"],
        "private_key_id": CREDENTIALS["private_key_id"],
        "private_key": CREDENTIALS["private_key"],
        "client_email": CREDENTIALS["client_email"],
        "client_id": CREDENTIALS["client_id"],
        "auth_uri": CREDENTIALS["auth_uri"],
        "token_uri": CREDENTIALS["token_uri"],
        "auth_provider_x509_cert_url": CREDENTIALS["auth_provider_x509_cert_url"],
        "client_x509_cert_url": CREDENTIALS["client_x509_cert_url"],
    }
)
