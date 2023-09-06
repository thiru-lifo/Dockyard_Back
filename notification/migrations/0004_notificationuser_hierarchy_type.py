# Generated by Django 4.0.2 on 2023-08-07 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0003_remove_notificationuser_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='notificationuser',
            name='hierarchy_type',
            field=models.SmallIntegerField(choices=[(1, 'Recommender'), (2, 'Approver')], default=1),
            preserve_default=False,
        ),
    ]