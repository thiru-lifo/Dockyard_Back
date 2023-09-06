# Generated by Django 4.0.2 on 2023-07-31 05:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0009_formlevelhierarchy'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectlevelhierarchy',
            name='approver',
        ),
        migrations.RemoveField(
            model_name='projectlevelhierarchy',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='projectlevelhierarchy',
            name='form',
        ),
        migrations.RemoveField(
            model_name='projectlevelhierarchy',
            name='project',
        ),
        migrations.RemoveField(
            model_name='projectlevelhierarchy',
            name='recommender',
        ),
        migrations.DeleteModel(
            name='FormLevelHierarchy',
        ),
        migrations.DeleteModel(
            name='ProjectLevelHierarchy',
        ),
    ]
