# Generated by Django 4.0.2 on 2023-08-17 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0018_alter_formlevelrecommenderhierarchy_recommender_level_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formlevelrecommenderhierarchy',
            name='recommender_level_status',
            field=models.SmallIntegerField(choices=[(1, 'accept'), (2, 'reject'), (-1, 'inital')], default=-1),
        ),
    ]
