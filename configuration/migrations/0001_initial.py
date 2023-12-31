# Generated by Django 4.0.2 on 2023-07-13 15:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('access', '0002_initial'),
        ('master', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Configurationtable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(default='', max_length=100)),
                ('default_values', models.TextField(default='', null=True)),
                ('value', models.TextField(default='', null=True)),
                ('code', models.CharField(default='', max_length=100)),
                ('isCenter', models.BooleanField(default=False)),
                ('status', models.SmallIntegerField(choices=[(1, 'Active'), (2, 'Inactive'), (3, 'Delete')])),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Configuration_table',
                'verbose_name_plural': 'Configuration_table',
                'db_table': 'configuration.Configuration_table',
            },
        ),
        migrations.CreateModel(
            name='Templatestable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=100)),
                ('type', models.SmallIntegerField(choices=[(1, 'Email'), (2, 'PDF')], default=1)),
                ('actual_template', models.TextField(default='', null=True)),
                ('modified_template', models.TextField(default='', null=True)),
                ('modified_on', models.DateTimeField(auto_now=True, null=True)),
                ('modified_by', models.CharField(blank=True, max_length=100, null=True)),
                ('modified_ip', models.GenericIPAddressField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'common teamplate',
                'verbose_name_plural': 'Common Templates',
                'db_table': 'configuration.templates',
            },
        ),
        migrations.CreateModel(
            name='TemplatesCountry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actual_template', models.TextField(default='', null=True)),
                ('modified_template', models.TextField(default='', null=True)),
                ('modified_on', models.DateTimeField(auto_now=True, null=True)),
                ('modified_by', models.CharField(blank=True, max_length=100, null=True)),
                ('modified_ip', models.GenericIPAddressField(blank=True, null=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master.countries')),
                ('template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuration.templatestable')),
            ],
            options={
                'verbose_name': 'teamplate_country',
                'verbose_name_plural': 'Template Countries',
                'db_table': 'configuration.templates_country',
            },
        ),
        migrations.CreateModel(
            name='RoleConfiguration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('config', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuration.configurationtable')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='access.accessuserroles')),
            ],
            options={
                'verbose_name': 'Center_Configuration',
                'verbose_name_plural': 'Center_Configuration',
                'db_table': 'configuration.role_configuration',
            },
        ),
        migrations.CreateModel(
            name='Approval',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.SmallIntegerField(choices=[(1, 'First Level'), (2, 'Second Level'), (3, 'Three Level'), (4, 'Fourth Level'), (5, 'Fifth Level')], null=True)),
                ('status', models.SmallIntegerField(choices=[(1, 'Active'), (2, 'Inactive'), (3, 'Delete')], default=1)),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_ip', models.GenericIPAddressField(blank=True, null=True)),
                ('modified_on', models.DateTimeField(auto_now=True, null=True)),
                ('modified_ip', models.GenericIPAddressField(blank=True, null=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_by', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='modified_by', to=settings.AUTH_USER_MODEL)),
                ('user_role', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='access.accessuserroles')),
            ],
            options={
                'verbose_name': 'Approval',
                'verbose_name_plural': 'Approval',
                'db_table': 'configuration.approval',
            },
        ),
    ]
