# Generated by Django 5.0.1 on 2024-03-18 14:04

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="task",
            old_name="desc",
            new_name="taskDesc",
        ),
    ]
