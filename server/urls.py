# -*- coding: utf-8 -*-

"""
Main URL mapping configuration file.

Include other URLConfs from external apps using method `include()`.

It is also a good practice to keep a single URL to the root index page.

This examples uses Django's default media
files serving technique in development.
"""
import json
from urllib.parse import urljoin

from server.settings.components import config
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from telegram import Update
from telegram.ext import Updater

from server.api import urlpatterns as api_urlpatterns
from server.apps.common.utils import dispatcher, bot


@method_decorator(csrf_exempt, name='dispatch')
class SetWebHook(View):
    print('hello')

    def get(self, request, *args, **kwargs):
        print('webhook')
        updater = Updater(config('TELEGRAM_BOT_TOKEN'))
        r=updater.bot.set_webhook(urljoin(config('TG_WEBHOOK'), '/tg/message/'))
        print(r)
        return HttpResponse('webhook')


@method_decorator(csrf_exempt, name='dispatch')
class Home(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('ok')

    def post(self, request, *args, **kwargs):
        update = Update.de_json(json.loads(request.body), bot)
        dispatcher.process_update(update)
        return HttpResponse('ok')


urlpatterns = [
    url('tg/message/', Home.as_view()),
    url('tg/set_webhook/', SetWebHook.as_view()),
    url('admin/', admin.site.urls),
] + api_urlpatterns


if settings.DEBUG:  # pragma: no cover
    import debug_toolbar
    from django.views.static import serve

    urlpatterns = [
        # URLs specific only to django-debug-toolbar:
        url(r'^__debug__/', include(debug_toolbar.urls)),

        # Serving media files in development only:
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ] + urlpatterns
