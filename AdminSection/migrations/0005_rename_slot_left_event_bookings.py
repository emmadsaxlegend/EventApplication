# Generated by Django 4.1.3 on 2023-01-01 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("AdminSection", "0004_delete_slot_alter_event_slot_left"),
    ]

    operations = [
        migrations.RenameField(
            model_name="event", old_name="slot_left", new_name="bookings",
        ),
    ]
