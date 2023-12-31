# Generated by Django 4.1.3 on 2023-09-28 01:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HotelApis', '0002_hoteldrinksproducts_storebincode_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='HotelProductsUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Unit', models.CharField(max_length=500, verbose_name='Unit')),
                ('Description', models.TextField(blank=True, max_length=500, null=True, verbose_name='Description')),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Hotel Products Unit',
            },
        ),
        migrations.AddField(
            model_name='hoteldrinksproducts',
            name='Unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='HotelApis.hotelproductsunit', verbose_name='Product Unit'),
        ),
        migrations.AddField(
            model_name='hotelfoodproducts',
            name='Unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='HotelApis.hotelproductsunit', verbose_name='Product Unit'),
        ),
        migrations.AddField(
            model_name='hotelrooms',
            name='Unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='HotelApis.hotelproductsunit', verbose_name='Product Unit'),
        ),
    ]
