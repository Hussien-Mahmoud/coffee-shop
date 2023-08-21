"""
WSGI config for coffee_shop project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

# To load environment variables from .env
from dotenv import load_dotenv
load_dotenv(override=False)

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coffee_shop.settings.local')

application = get_wsgi_application()
