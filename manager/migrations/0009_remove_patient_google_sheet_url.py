# Generated by Django 4.2.13 on 2024-07-03 22:01

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("manager", "0008_remove_clientsession_diet_plan_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="patient",
            name="google_sheet_url",
        ),
    ]
