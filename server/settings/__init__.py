# -*- coding: utf-8 -*-

"""
This is a django-split-settings main file.

For more information read this:
https://github.com/sobolevn/django-split-settings

To change settings file:
`DJANGO_ENV=production python manage.py runserver`
"""

from os import environ

from split_settings.tools import optional, include


# Managing environment via DJANGO_ENV variable:
environ.setdefault('DJANGO_ENV', 'development')
ENV = environ['DJANGO_ENV']

base_settings = [
    'components/apps.py',
    'components/common.py',
    'components/database.py',
    'components/drf.py',
    'components/internationalization.py',
    'components/logging.py',
    'components/caches.py',
    'components/celery.py',
    'components/templates.py',
    'components/static.py',
    'components/swagger.py',

    # You can even use glob:
    # 'components/*.py'

    # Select the right env:
    'environments/{0}.py'.format(ENV),

    # Optionally override some settings:
    optional('environments/local.py'),
]

# Include settings:
include(*base_settings)
