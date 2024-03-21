# Generated by Django 4.1.7 on 2023-12-01 19:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("nft_tokens", "0011_alter_pack_price_alter_token_price"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pack",
            name="price",
            field=models.PositiveIntegerField(
                help_text="Цена в копейках", verbose_name="price"
            ),
        ),
        migrations.AlterField(
            model_name="token",
            name="price",
            field=models.PositiveIntegerField(
                help_text="Цена в копейках", verbose_name="price"
            ),
        ),
    ]
