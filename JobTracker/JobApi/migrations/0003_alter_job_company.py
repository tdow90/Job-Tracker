# Generated by Django 5.1.4 on 2025-01-12 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JobApi', '0002_alter_job_link_alter_job_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='company',
            field=models.CharField(max_length=200),
        ),
    ]