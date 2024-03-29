# Generated by Django 4.2.8 on 2023-12-12 14:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('details', models.TextField()),
                ('representative', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Object',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('responsible', models.CharField(max_length=255)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='applications.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Performer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_request_number', models.CharField(max_length=255)),
                ('responsible_customer', models.CharField(max_length=255)),
                ('request_text', models.TextField()),
                ('department', models.CharField(max_length=255)),
                ('request_date', models.DateField()),
                ('status', models.BooleanField(default=False)),
                ('completion_date', models.DateField(blank=True, null=True)),
                ('act', models.TextField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('estimate_number', models.CharField(max_length=255)),
                ('budget_line_code', models.CharField(max_length=255)),
                ('agreed_budget_number', models.CharField(max_length=255)),
                ('budget_type', models.CharField(max_length=255)),
                ('budget_name', models.CharField(max_length=255)),
                ('period', models.CharField(max_length=255)),
                ('amount_with_vat', models.DecimalField(decimal_places=2, max_digits=10)),
                ('simple_closure', models.BooleanField(default=False)),
                ('invoice_number', models.CharField(blank=True, max_length=255, null=True)),
                ('payment_date', models.DateField(blank=True, null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='applications.customer')),
                ('object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='applications.object')),
                ('performer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='applications.performer')),
            ],
        ),
    ]
