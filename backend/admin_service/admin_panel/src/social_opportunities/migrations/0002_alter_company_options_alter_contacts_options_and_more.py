# Generated by Django 4.1.7 on 2023-10-24 12:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("social_opportunities", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="company",
            options={
                "ordering": ("-created_at",),
                "verbose_name": "1 - Компания",
                "verbose_name_plural": "1 - Компании",
            },
        ),
        migrations.AlterModelOptions(
            name="contacts",
            options={
                "ordering": ("-created_at",),
                "verbose_name": "3 - Контакт",
                "verbose_name_plural": "3 - Контакты",
            },
        ),
        migrations.AlterModelOptions(
            name="reviewcompanymoderator",
            options={
                "ordering": ("-created_at",),
                "verbose_name": "4 - Отзыв компании",
                "verbose_name_plural": "4 - Отзывы компании",
            },
        ),
        migrations.AlterModelOptions(
            name="reviewservicemoderator",
            options={
                "ordering": ("-created_at",),
                "verbose_name": "5 - Отзыв сервиса",
                "verbose_name_plural": "5 - Отзывы сервиса",
            },
        ),
        migrations.AlterModelOptions(
            name="service",
            options={
                "ordering": ("-created_at",),
                "verbose_name": "2 - Сервис",
                "verbose_name_plural": "2 - Сервисы",
            },
        ),
        migrations.AlterField(
            model_name="company",
            name="logo",
            field=models.ImageField(
                upload_to="company/",
                validators=[
                    django.core.validators.FileExtensionValidator(
                        ["jpeg", "jpg", "png"]
                    )
                ],
                verbose_name="Лого",
            ),
        ),
    ]
