# Generated by Django 4.0.2 on 2023-08-24 06:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0028_globaltransactionshipdetail_ship_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='globaltransactionshipdetail',
            name='form',
        ),
    ]
