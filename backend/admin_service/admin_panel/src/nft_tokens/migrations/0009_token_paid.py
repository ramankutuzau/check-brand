# Generated by Django 4.1.7 on 2023-12-01 19:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("nft_tokens", "0008_alter_collection_symbol"),
    ]

    operations = [
        migrations.AddField(
            model_name="token",
            name="paid",
            field=models.BooleanField(default=False, verbose_name="paid"),
        ),
    ]
