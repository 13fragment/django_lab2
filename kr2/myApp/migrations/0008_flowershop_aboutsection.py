# Generated by Django 5.2.1 on 2025-05-25 13:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myApp", "0007_student_teacher_classmate"),
    ]

    operations = [
        migrations.CreateModel(
            name="FlowerShop",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("tagline", models.CharField(max_length=200)),
                ("description", models.TextField()),
                ("delivery_info", models.CharField(max_length=200)),
                (
                    "main_image",
                    models.ImageField(default="home.jpg", upload_to="shop_images/"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="AboutSection",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("content", models.TextField()),
                (
                    "shop",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="about_sections",
                        to="myApp.flowershop",
                    ),
                ),
            ],
        ),
    ]
