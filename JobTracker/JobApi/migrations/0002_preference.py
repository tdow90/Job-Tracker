# Generated by Django 5.1.4 on 2025-01-04 17:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JobApi', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Preference',
            fields=[
                ('User', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('city', models.CharField(max_length=100)),
                ('job_type', models.CharField(max_length=100)),
            ],
        ),
    ]
