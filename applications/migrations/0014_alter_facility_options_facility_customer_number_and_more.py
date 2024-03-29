# Generated by Django 4.2.8 on 2024-01-13 15:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('applications', '0013_facility'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='facility',
            options={'ordering': ['customer__name', 'title'], 'verbose_name': 'Объект', 'verbose_name_plural': 'Объекты'},
        ),
        migrations.AddField(
            model_name='facility',
            name='customer_number',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='номер в системе заказчика'),
        ),
        migrations.AddField(
            model_name='facility',
            name='responsible',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=models.SET(None), to=settings.AUTH_USER_MODEL),
        ),
    ]
