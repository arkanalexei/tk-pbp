# Generated by Django 4.1 on 2022-10-27 10:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="WasteDeposit",
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
                ("mass", models.FloatField()),
                ("description", models.TextField()),
                ("date_time", models.DateField(default=django.utils.timezone.now)),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("PLASTIK", "Plastik"),
                            ("KACA", "Kaca / Beling"),
                            ("KERTAS", "Kertas / Kardus"),
                            ("ETC", "Organik & Lainnya"),
                        ],
                        default=("PLASTIK", "Plastik"),
                        max_length=32,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
