# Generated by Django 4.1.3 on 2022-12-09 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("AdminSection", "0002_rename_freeevent_free"),
    ]

    operations = [
        migrations.RenameModel(old_name="PaidEvent", new_name="Event",),
        migrations.DeleteModel(name="Free",),
    ]
