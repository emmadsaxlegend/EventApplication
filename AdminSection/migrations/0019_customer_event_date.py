# Generated by Django 4.1.3 on 2023-01-10 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("AdminSection", "0018_alter_customer_event_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="customer",
            name="event_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]