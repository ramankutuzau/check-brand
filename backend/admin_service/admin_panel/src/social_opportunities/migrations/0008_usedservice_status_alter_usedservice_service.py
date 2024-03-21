# Generated by Django 4.1.7 on 2023-12-03 11:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("social_opportunities", "0007_usedservice_service_token_uniq"),
    ]

    operations = [
        migrations.AddField(
            model_name="usedservice",
            name="status",
            field=models.CharField(
                choices=[
                    ("clicked", "Clicked"),
                    ("used", "Used"),
                    ("not_used", "Not used"),
                ],
                default="not_used",
                max_length=15,
            ),
        ),
        migrations.AlterField(
            model_name="usedservice",
            name="service",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="used",
                to="social_opportunities.service",
            ),
        ),
    ]