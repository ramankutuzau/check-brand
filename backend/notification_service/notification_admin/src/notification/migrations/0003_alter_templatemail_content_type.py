# Generated by Django 4.1.6 on 2023-02-03 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0002_remove_templatemail_body_remove_templatemail_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='templatemail',
            name='content_type',
            field=models.CharField(choices=[('test', 'Test'), ('added_white_list', 'added_white_list'), ('booking_started', 'booking_started'), ('added_white_list_and_booking', 'added_white_list_and_booking'), ('user_booked', 'user_booked'), ('minting_1_started', 'minting_1_started'), ('added_white_and_expects', 'added_white_and_expects'), ('minting_2_started', 'minting_2_started'), ('added_white_list_and_minting_2', 'added_white_list_and_minting_2'), ('user_minted', 'user_minted'), ('minting_stopped', 'minting_stopped')], default='test', max_length=64, unique=True, verbose_name='content type'),
        ),
    ]
