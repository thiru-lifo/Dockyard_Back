# Generated by Django 4.0.2 on 2023-08-22 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0024_formlevelrecommenderhierarchy_current_reject_level'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formlevelrecommenderhierarchy',
            name='current_reject_level',
        ),
    ]