# Generated by Django 4.1.1 on 2022-09-23 22:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("kanban", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="task",
            old_name="name",
            new_name="title",
        ),
    ]
