"""
WSGI config for eventex project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
from dj_static import Cling
from django.core.wsgi import get_wsgi_application
from decouple import config

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eventex.settings')

USE_S3 = config('USE_S3', default=False, cast=bool)

if USE_S3:
    application = get_wsgi_application()
else:
    application = Cling(get_wsgi_application())
