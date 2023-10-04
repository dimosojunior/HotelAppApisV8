# Generated by Django 4.1.3 on 2023-10-01 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RetailsApis', '0004_retailsdrinksorder_order_status_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='RetailsSuppliers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SupplierFullName', models.CharField(max_length=500, verbose_name='Supplier Full Name')),
                ('PhoneNumber', models.CharField(blank=True, default='+255', max_length=14, null=True, verbose_name='Phone Number')),
                ('SupplierAddress', models.CharField(blank=True, max_length=200, null=True, verbose_name='Supplier Address')),
                ('Status', models.CharField(blank=True, choices=[('Active', 'Active'), ('Passive', 'Passive')], default='Active', max_length=200, null=True, verbose_name='Status')),
                ('Keyword', models.CharField(blank=True, max_length=500, null=True, verbose_name='Keyword')),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Retails Suppliers',
            },
        ),
    ]
