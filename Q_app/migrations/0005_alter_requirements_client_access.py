# Generated by Django 4.1.4 on 2023-07-14 07:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Q_app", "0004_rename_option_requirements_sel_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="requirements",
            name="client_access",
            field=models.CharField(max_length=200),
        ),
    ]
