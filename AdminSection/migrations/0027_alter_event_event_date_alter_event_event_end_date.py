# Generated by Django 4.1.3 on 2023-01-27 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "AdminSection",
            "0026_remove_event_time_field_alter_event_event_date_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="event_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="event",
            name="event_end_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]