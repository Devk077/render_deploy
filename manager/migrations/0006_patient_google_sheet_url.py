# Generated by Django 4.2.13 on 2024-06-29 08:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("manager", "0005_alter_session_body_composition_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="patient",
            name="google_sheet_url",
            field=models.URLField(blank=True, null=True),
        ),
    ]
