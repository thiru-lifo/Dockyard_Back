# Generated by Django 4.0.2 on 2023-08-21 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0004_ships'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='equipment_ship_id',
            field=models.IntegerField(null=True),
        ),
    ]
