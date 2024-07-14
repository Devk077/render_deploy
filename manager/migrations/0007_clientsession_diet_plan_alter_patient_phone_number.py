# Generated by Django 4.2.13 on 2024-07-02 20:25

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):
    dependencies = [
        ("manager", "0006_patient_google_sheet_url"),
    ]

    operations = [
        migrations.AddField(
            model_name="clientsession",
            name="diet_plan",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="patient",
            name="phone_number",
            field=phonenumber_field.modelfields.PhoneNumberField(
                default="+91", max_length=128, null=True, region=None
            ),
        ),
    ]