# Generated by Django 4.0.2 on 2023-07-31 05:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0011_projectlevelrecommenderhierarchy_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formlevelrecommenderhierarchy',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='formlevelrecommenderhierarchy',
            name='form',
        ),
        migrations.RemoveField(
            model_name='formlevelrecommenderhierarchy',
            name='recommender',
        ),
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
            model_name='projectlevelrecommenderhierarchy',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='projectlevelrecommenderhierarchy',
            name='form',
        ),
        migrations.RemoveField(
            model_name='projectlevelrecommenderhierarchy',
            name='project',
        ),
        migrations.RemoveField(
            model_name='projectlevelrecommenderhierarchy',
            name='recommender',
        ),
        migrations.DeleteModel(
            name='FormLevelApproverHierarchy',
        ),
        migrations.DeleteModel(
            name='FormLevelRecommenderHierarchy',
        ),
        migrations.DeleteModel(
            name='ProjectLevelHierarchy',
        ),
        migrations.DeleteModel(
            name='ProjectLevelRecommenderHierarchy',
        ),
    ]
