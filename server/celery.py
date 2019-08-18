import os

from celery import Celery

from server.settings.components.apps import INSTALLED_APPS

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')

app = Celery('server')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: INSTALLED_APPS)
app.conf.broker_url = 'redis://redis:6379/0'


@app.task(bind=True)
def debug_task(self, **kwargs):
    """Debug task."""
    logger = debug_task.get_logger(**kwargs)
    logger.warn('Request: {0!r}'.format(self.request))
