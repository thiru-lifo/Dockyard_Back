# Generated by Django 4.0.2 on 2023-07-13 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccessModules',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.TextField()),
                ('status', models.SmallIntegerField(choices=[(1, 'Active'), (2, 'Inactive'), (3, 'Delete')])),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(max_length=100)),
                ('created_ip', models.GenericIPAddressField()),
                ('modified_on', models.DateTimeField(auto_now=True, null=True)),
                ('modified_by', models.CharField(blank=True, max_length=100, null=True)),
                ('modified_ip', models.GenericIPAddressField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Access Modules',
                'verbose_name_plural': 'Access Modules',
                'db_table': 'access.access_modules',
            },
        ),
        migrations.CreateModel(
            name='AccessUserRoles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_ad', models.CharField(max_length=200, null=True)),
                ('name', models.CharField(default='', max_length=200)),
                ('code', models.CharField(default='', max_length=10, unique=True)),
                ('is_biometric', models.BooleanField(default=False)),
                ('modified_on', models.DateTimeField(auto_now=True, null=True)),
                ('modified_by', models.CharField(blank=True, max_length=100, null=True)),
                ('modified_ip', models.GenericIPAddressField(blank=True, null=True)),
                ('status', models.SmallIntegerField(choices=[(1, 'Active'), (2, 'Inactive'), (3, 'Delete')], default=1)),
            ],
            options={
                'verbose_name': 'Access User roles',
                'verbose_name_plural': 'Access User roles',
                'db_table': 'access.user_roles',
            },
        ),
        migrations.CreateModel(
            name='Modules',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=150)),
                ('url', models.CharField(default='', max_length=500, null=True)),
                ('icon', models.CharField(default='', max_length=500)),
                ('sequence', models.IntegerField(null=True)),
                ('action', models.TextField()),
                ('status', models.SmallIntegerField(choices=[(1, 'Active'), (2, 'Inactive'), (3, 'Delete')])),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(max_length=100)),
                ('created_ip', models.GenericIPAddressField()),
                ('modified_on', models.DateTimeField(auto_now=True, null=True)),
                ('modified_by', models.CharField(blank=True, max_length=100, null=True)),
                ('modified_ip', models.GenericIPAddressField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Modules',
                'verbose_name_plural': 'Modules',
                'db_table': 'access.modules',
            },
        ),
        migrations.CreateModel(
            name='ModulesComponents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=150)),
                ('sequence', models.IntegerField(null=True)),
                ('url', models.CharField(max_length=500, null=True)),
                ('icon', models.CharField(default='', max_length=500)),
                ('action', models.TextField()),
                ('status', models.SmallIntegerField(choices=[(1, 'Active'), (2, 'Inactive'), (3, 'Delete')])),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(max_length=100)),
                ('created_ip', models.GenericIPAddressField()),
                ('modified_on', models.DateTimeField(auto_now=True, null=True)),
                ('modified_by', models.CharField(blank=True, max_length=100, null=True)),
                ('modified_ip', models.GenericIPAddressField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'ModulesComponents',
                'verbose_name_plural': 'ModulesComponents',
                'db_table': 'access.modules_components',
            },
        ),
        migrations.CreateModel(
            name='ModulesComponentsAttributes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=150)),
                ('sequence', models.IntegerField(null=True)),
                ('action', models.TextField()),
                ('url', models.CharField(max_length=500, null=True)),
                ('icon', models.CharField(default='', max_length=500)),
                ('status', models.SmallIntegerField(choices=[(1, 'Active'), (2, 'Inactive'), (3, 'Delete')])),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(max_length=100)),
                ('created_ip', models.GenericIPAddressField()),
                ('modified_on', models.DateTimeField(auto_now=True, null=True)),
                ('modified_by', models.CharField(blank=True, max_length=100, null=True)),
                ('modified_ip', models.GenericIPAddressField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Modules Components Attributes',
                'verbose_name_plural': 'Modules Components Attributes',
                'db_table': 'access.modules_components_attributes',
            },
        ),
        migrations.CreateModel(
            name='Privileges',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('code', models.CharField(max_length=150)),
                ('sequence', models.IntegerField(null=True)),
                ('status', models.SmallIntegerField(choices=[(1, 'Active'), (2, 'Inactive'), (3, 'Delete')])),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(max_length=100)),
                ('created_ip', models.GenericIPAddressField()),
                ('modified_on', models.DateTimeField(auto_now=True, null=True)),
                ('modified_by', models.CharField(blank=True, max_length=100, null=True)),
                ('modified_ip', models.GenericIPAddressField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Access Privileges',
                'verbose_name_plural': 'Access Privileges',
                'db_table': 'access.privileges',
            },
        ),
        migrations.CreateModel(
            name='Process',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('sequence', models.IntegerField(null=True)),
            ],
            options={
                'verbose_name': 'Process',
                'verbose_name_plural': 'Processes',
                'db_table': 'access.process',
            },
        ),
        migrations.CreateModel(
            name='ProcessFlow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.SmallIntegerField()),
            ],
            options={
                'verbose_name': 'process_flow',
                'verbose_name_plural': 'process_flow',
                'db_table': 'access.process_flow',
            },
        ),
        migrations.CreateModel(
            name='ProcessRoleMapping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'process_role_mapping',
                'verbose_name_plural': 'process_role_mapping',
                'db_table': 'access.process_role_mapping',
            },
        ),
        migrations.CreateModel(
            name='RolesPermissions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permissions', models.TextField()),
            ],
            options={
                'verbose_name': 'Permission',
                'verbose_name_plural': 'Permissions',
                'db_table': 'access.roles_permission',
            },
        ),
        migrations.CreateModel(
            name='UserRoleDesignation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.IntegerField(null=True)),
                ('status', models.SmallIntegerField(choices=[(1, 'Active'), (2, 'Inactive'), (3, 'Delete')])),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(max_length=100)),
                ('created_ip', models.GenericIPAddressField()),
                ('modified_on', models.DateTimeField(auto_now=True, null=True)),
                ('modified_by', models.CharField(blank=True, max_length=100, null=True)),
                ('modified_ip', models.GenericIPAddressField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'UserRoleDesignation',
                'verbose_name_plural': 'UserRoleDesignation',
                'db_table': 'access.user_role_designation',
            },
        ),
        migrations.CreateModel(
            name='UserRoleMapping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('default', models.SmallIntegerField(choices=[(1, 'Default center'), (0, 'Non default')], null=True)),
                ('process', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='access.process')),
            ],
            options={
                'verbose_name': 'User Role Mapping',
                'verbose_name_plural': 'Users Roles Mapping',
                'db_table': 'access.user_role_mapping',
            },
        ),
    ]
