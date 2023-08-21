from .local import *
import os
from google.oauth2 import service_account


STORAGES["default"] = {"BACKEND": "storages.backends.gcloud.GoogleCloudStorage"}

GS_BUCKET_NAME = os.environ['GS_BUCKET_NAME']
GS_CREDENTIALS = service_account.Credentials.from_service_account_file('credentials.json')
GS_IS_GZIPPED = True