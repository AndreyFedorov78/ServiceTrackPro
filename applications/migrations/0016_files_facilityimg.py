# Generated by Django 4.2.8 on 2024-01-20 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0015_facility_region'),
    ]

    operations = [
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('file_name', models.CharField(max_length=255, verbose_name='Имя загруженного файла')),
                ('real_file_name', models.CharField(max_length=255, verbose_name='Имя файла на диске')),
            ],
        ),
        migrations.CreateModel(
            name='FacilityIMG',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('facility', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='applications.facility')),
                ('file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='applications.files')),
            ],
        ),
    ]
