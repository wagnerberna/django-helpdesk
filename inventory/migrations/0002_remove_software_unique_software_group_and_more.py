# Generated by Django 4.1.5 on 2023-03-28 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='software',
            name='unique_software_group',
        ),
        migrations.AddConstraint(
            model_name='software',
            constraint=models.UniqueConstraint(fields=('operating_system', 'operating_system_version', 'architecture'), name='unique_software_group'),
        ),
    ]
