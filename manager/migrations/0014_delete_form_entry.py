# Generated by Django 4.2.13 on 2024-07-13 12:49

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("manager", "0013_rename_messsage_form_entry_message"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Form_Entry",
        ),
    ]
