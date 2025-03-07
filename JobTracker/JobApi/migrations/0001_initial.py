# Generated by Django 5.1.4 on 2025-01-12 22:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Preference',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='user_profile', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('city', models.CharField(max_length=100)),
                ('job_type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('link', models.URLField(max_length=191)),
                ('company', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('date_posted', models.DateField(blank=True, null=True)),
                ('job_details', models.TextField(max_length=500)),
                ('description', models.TextField(max_length=1000)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'unique_together': {('title', 'company', 'link')},
            },
        ),
    ]
