# Generated by Django 4.1.4 on 2023-07-13 05:32

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("Q_app", "0003_requirements_client_access_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="requirements",
            old_name="option",
            new_name="sel_options",
        ),
    ]
