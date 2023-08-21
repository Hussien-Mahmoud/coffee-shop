from .local_cloud_files import *

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