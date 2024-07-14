# Generated by Django 4.2.13 on 2024-07-02 20:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("manager", "0007_clientsession_diet_plan_alter_patient_phone_number"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="clientsession",
            name="diet_plan",
        ),
        migrations.AddField(
            model_name="clientsession",
            name="patient_url",
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name="clientsession",
            name="patient",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to="manager.patient"
            ),
        ),
    ]