# Generated by Django 4.1.3 on 2023-01-06 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("AdminSection", "0012_customer"),
    ]

    operations = [
        migrations.RenameField(
            model_name="customer", old_name="event_name", new_name="event_id",
        ),
        migrations.RemoveField(model_name="customer", name="name",),
    ]
