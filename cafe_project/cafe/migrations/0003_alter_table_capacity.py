# Generated by Django 5.1.6 on 2025-02-17 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0002_menuitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='capacity',
            field=models.IntegerField(default=4),
        ),
    ]
