# Generated by Django 4.2.13 on 2024-07-10 12:59

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):
    dependencies = [
        ("manager", "0011_alter_session_session_date"),
    ]

    operations = [
        migrations.CreateModel(
            name="Form_Entry",
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
                ("name", models.CharField(max_length=100)),
                (
                    "ph",
                    phonenumber_field.modelfields.PhoneNumberField(
                        default="+91", max_length=128, null=True, region=None
                    ),
                ),
                ("messsage", models.TextField(blank=True, default="", null=True)),
            ],
        ),
        migrations.AlterField(
            model_name="bodycomposition",
            name="height",
            field=models.FloatField(verbose_name="Height (Cm)"),
        ),
    ]