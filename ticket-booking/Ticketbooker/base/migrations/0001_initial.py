# Generated by Django 5.1.4 on 2024-12-19 03:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="StageEvent",
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
                ("name", models.CharField(max_length=25)),
                ("detail", models.CharField(max_length=25)),
                ("organizer", models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name="StageEventShow",
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
                ("start_time", models.DateTimeField(null=True)),
                ("end_time", models.DateTimeField(null=True)),
                (
                    "stage_event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="base.stageevent",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TicketBooking",
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
                ("price", models.FloatField()),
                ("customer", models.CharField(max_length=45)),
                ("no_of_seats", models.FloatField()),
                (
                    "stage_event_show",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="base.stageeventshow",
                    ),
                ),
            ],
        ),
    ]