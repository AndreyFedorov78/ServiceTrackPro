# Generated by Django 4.2.8 on 2024-01-01 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0003_alter_object_responsible'),
    ]

    operations = [
        migrations.AlterField(
            model_name='object',
            name='responsible',
            field=models.CharField(default='', max_length=255, null=True),
        ),
    ]
