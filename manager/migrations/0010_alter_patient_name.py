# Generated by Django 4.2.13 on 2024-07-03 22:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("manager", "0009_remove_patient_google_sheet_url"),
    ]

    operations = [
        migrations.AlterField(
            model_name="patient",
            name="name",
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
