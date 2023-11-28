# Generated by Django 4.2.6 on 2023-11-28 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CategoriesModel",
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
                (
                    "name",
                    models.TextField(
                        help_text="название категории профессии",
                        verbose_name="категория",
                    ),
                ),
            ],
            options={
                "verbose_name": "категория",
                "verbose_name_plural": "категории",
            },
        ),
        migrations.CreateModel(
            name="ProfessionsModel",
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
                (
                    "name",
                    models.TextField(
                        help_text="название профессии", verbose_name="название"
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        help_text="описание профессии", verbose_name="описание"
                    ),
                ),
                (
                    "wage",
                    models.TextField(
                        help_text="заработная плата",
                        verbose_name="заработная плата"
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        help_text="к какой категории относится профессия",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="professions.categoriesmodel",
                    ),
                ),
            ],
            options={
                "verbose_name": "профессия",
                "verbose_name_plural": "профессии",
            },
        ),
    ]