from django.conf import settings
from EcpDemo.celery import app
from datetime import timedelta
from datetime import datetime, timedelta
from celery.schedules import crontab
from django.core.mail import send_mail


@app.task(name="print_test")
def print_test():
    #get_premiums()
    print("*****#####- Rabbitmq & Celery is Running ####*******")


app.conf.beat_schedule = {
    'run-every-8-seconds': {
        'task': 'print_test',
        'schedule': 8
    }
}
