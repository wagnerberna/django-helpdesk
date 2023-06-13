# Generated by Django 4.1.5 on 2023-05-17 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("ti", "0001_initial"),
        ("inventory", "0004_rename_link_server_url_external_server_url_internal"),
    ]

    operations = [
        migrations.CreateModel(
            name="SwitchManufacturer",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=20, null=True, unique=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "db_table": "inventory_switch_manufacturer",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="SwitchModel",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=30, null=True, unique=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "db_table": "inventory_switch_model",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="SwitchHardware",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "manufacturer",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="inventory.switchmanufacturer",
                    ),
                ),
                (
                    "model",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="inventory.switchmodel",
                    ),
                ),
            ],
            options={
                "db_table": "inventory_switch_hardware",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="Switch",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("inventory", models.IntegerField(null=True, unique=True)),
                (
                    "user",
                    models.CharField(blank=True, max_length=15, null=True, unique=True),
                ),
                (
                    "password",
                    models.CharField(blank=True, max_length=15, null=True, unique=True),
                ),
                ("ip", models.CharField(blank=True, max_length=15, null=True)),
                ("stack", models.BooleanField(default=False)),
                ("url_access", models.CharField(blank=True, max_length=30, null=True)),
                ("mac", models.CharField(blank=True, max_length=17, null=True)),
                ("detail", models.CharField(blank=True, max_length=200, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "department",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ti.department",
                    ),
                ),
                (
                    "status",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="inventory.statussituation",
                    ),
                ),
                (
                    "switch_hardware",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="inventory.switchhardware",
                    ),
                ),
            ],
            options={
                "db_table": "inventory_switch",
                "managed": True,
            },
        ),
        migrations.AddConstraint(
            model_name="switchhardware",
            constraint=models.UniqueConstraint(
                fields=("manufacturer", "model"), name="unique_switch_group"
            ),
        ),
    ]