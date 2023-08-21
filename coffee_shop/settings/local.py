from .base import *

SECRET_KEY='django-insecure-adlfkn;asrlfh3j0259o;KH&*$%76&*(tU('

DEBUG = False if os.environ.get('DEBUG') == 'False' else True   # the default is True
ALLOWED_HOSTS = ['*']
