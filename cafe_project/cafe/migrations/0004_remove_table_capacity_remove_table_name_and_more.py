# Generated by Django 4.2.18 on 2025-02-20 03:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cafe", "0003_alter_table_capacity"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="table",
            name="capacity",
        ),
        migrations.RemoveField(
            model_name="table",
            name="name",
        ),
        migrations.AddField(
            model_name="table",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True,
                default=datetime.datetime(
                    2025, 2, 20, 3, 20, 29, 409468, tzinfo=datetime.timezone.utc
                ),
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="table",
            name="qr_code",
            field=models.ImageField(blank=True, upload_to="qr_codes/"),
        ),
    ]
