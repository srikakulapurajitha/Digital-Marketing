# Generated by Django 4.1.4 on 2023-07-12 03:45

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("Q_app", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="requirements",
            name="planned_cost",
        ),
        migrations.RemoveField(
            model_name="user_report",
            name="total_cost",
        ),
    ]
