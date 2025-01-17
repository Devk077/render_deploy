# Generated by Django 4.2.13 on 2024-06-26 16:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("manager", "0004_bodycomposition_alter_patient_day_excercise_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="session",
            name="body_composition",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="manager.bodycomposition",
            ),
        ),
        migrations.AlterField(
            model_name="session",
            name="end_meal_line",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="session",
            name="session_date",
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name="session",
            name="start_meal_line",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name="ClientSession",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "patient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="manager.patient",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="session",
            name="client_session",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="client_session",
                to="manager.clientsession",
            ),
        ),
    ]
