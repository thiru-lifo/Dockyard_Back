# Generated by Django 4.0.2 on 2023-08-16 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0015_projectlevelapproverhierarchy'),
    ]

    operations = [
        migrations.AddField(
            model_name='globaltransaction',
            name='approver_level',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='globaltransaction',
            name='recommender_level',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
    ]