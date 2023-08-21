from .base import *
import os
from google.oauth2 import service_account

DEBUG = False
CSRF_TRUSTED_ORIGINS = os.environ.get('CSRF_TRUSTED_ORIGINS').split(',') or ['*']

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

STORAGES["default"] = {"BACKEND": "storages.backends.gcloud.GoogleCloudStorage"}

GS_BUCKET_NAME = os.environ['gs_bucket_name']
GS_CREDENTIALS = service_account.Credentials.from_service_account_file('credentials.json')
