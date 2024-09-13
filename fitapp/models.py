from django.conf import settings
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models

from fitapp.utils import get_datetime_next_day


class Ingredient(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    calories = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title[:25]


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)


class TrainingTask(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.TextField()
    date_from = models.DateTimeField(auto_now_add=True)
    date_end = models.DateTimeField(default=get_datetime_next_day)
    status = models.BooleanField(default=False)
    repeat = models.BooleanField(default=False)

    def __str__(self):
        return self.description[:100]

    def clean(self):
        if self.repeat:
            if TrainingTask.objects.filter(
                user=self.user, description=self.description, repeat=True
            ).exists():
                raise ValidationError(
                    "Task with this description and repeat=True already exists."
                )

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
