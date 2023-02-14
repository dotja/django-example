import os

from celery import Celery

## pass the settings module to the celery program
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_examples.settings')

## create the celery app instance
app = Celery('django_examples')

## add the django settings module as configuration source for celery
## i.e. configure celery directly from the django settings
## celery configuration is specified using uppercase CELERY
app.config_from_object('django.conf:settings', namespace='CELERY')

## celery will autodiscover tasks from all installed apps in our django project following the tasks.py convention
app.autodiscover_tasks()

