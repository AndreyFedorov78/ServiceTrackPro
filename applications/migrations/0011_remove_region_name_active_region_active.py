# Generated by Django 4.2.8 on 2024-01-12 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0010_region_name_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='region_name',
            name='active',
        ),
        migrations.AddField(
            model_name='region',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Активный'),
        ),
    ]
