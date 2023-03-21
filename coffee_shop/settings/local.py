from .base import *
import os
import json

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