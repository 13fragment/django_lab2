# Generated by Django 5.2.1 on 2025-05-21 14:39

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myApp", "0004_alter_contactrequest_options_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="contactrequest",
            name="created_at",
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name="Дата создания"
            ),
        ),
    ]
