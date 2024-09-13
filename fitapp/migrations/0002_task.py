# Generated by Django 5.0.4 on 2024-08-23 02:52

import django.db.models.deletion
import fitapp.utils
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fitapp", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Task",
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
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
