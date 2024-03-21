# Generated by Django 4.1.7 on 2023-12-23 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("nft_tokens", "0012_alter_pack_price_alter_token_price"),
        ("social_opportunities", "0011_applicationservice"),
    ]

    operations = [
        migrations.AlterField(
            model_name="applicationservice",
            name="token",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="application",
                to="nft_tokens.token",
            ),
        ),
    ]
