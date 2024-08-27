from datetime import timedelta

from django.utils import timezone


def get_datetime_next_day():
    return timezone.now() + timedelta(days=1)
