# Generated by Django 5.0.4 on 2024-09-13 13:21

import django.db.models.deletion
import fitapp.utils
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fitapp", "0002_task"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="TrainingTask",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("description", models.TextField()),
                ("date_from", models.DateTimeField(auto_now_add=True)),
                (
                    "date_end",
                    models.DateTimeField(default=fitapp.utils.get_datetime_next_day),
                ),
                ("status", models.BooleanField(default=False)),
                ("repeat", models.BooleanField(default=False)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="Task",
        ),
    ]
