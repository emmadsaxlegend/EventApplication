# Generated by Django 4.1.3 on 2022-12-30 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("AdminSection", "0002_rename_header_image_event_header_images"),
    ]

    operations = [
        migrations.CreateModel(
            name="Slot",
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
                ("slot_left", models.CharField(max_length=100)),
            ],
        ),
    ]
