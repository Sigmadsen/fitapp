import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fitapp.settings")

app = Celery("training_tasks")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()

app.conf.update(
    result_expires=3600,
)
