"""
WSGI config for vactest project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import site

site.addsitedir('/var/www/vactest/lib/python2.7/site-packages')

import os, sys

from django.core.wsgi import get_wsgi_application

sys.path.append('/var/www/vactest/bin/vactest')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vactest.settings")

application = get_wsgi_application()


