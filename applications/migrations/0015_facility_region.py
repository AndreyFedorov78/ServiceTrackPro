# Generated by Django 4.2.8 on 2024-01-13 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0014_alter_facility_options_facility_customer_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='facility',
            name='region',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=models.SET(None), to='applications.region'),
        ),
    ]
