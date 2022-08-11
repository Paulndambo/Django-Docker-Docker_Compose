from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab

#BROKER_URL = 'amqps://fsoievgp:Zgo2x6ZIYBDuVz4A-1ZnViUbxT0OLrV-@hawk.rmq.cloudamqp.com/fsoievgp'

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EcpDemo.settings')
app = Celery('EcpDemo')


app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
