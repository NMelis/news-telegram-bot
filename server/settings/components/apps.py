# -*- coding: utf-8 -*-

from typing import Tuple

# Application definition:

INSTALLED_APPS: Tuple[str, ...] = (
    # Default django apps:
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'djcelery',
    'drf_yasg',

    # django-admin:
    'django.contrib.admin',
    'django.contrib.admindocs',

    # Your apps go here:
    'server.apps.common',
    'server.apps.newsapi',
)
