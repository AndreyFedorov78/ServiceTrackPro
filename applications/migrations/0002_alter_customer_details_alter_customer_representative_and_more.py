# Generated by Django 4.2.8 on 2024-01-01 17:29

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('applications', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='details',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='representative',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='object',
            name='responsible',
            field=models.ForeignKey(default=None, null=True, on_delete=models.SET(None), to=settings.AUTH_USER_MODEL),
        ),
    ]