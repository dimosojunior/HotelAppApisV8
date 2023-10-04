# Generated by Django 4.1.3 on 2023-09-29 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HotelApis', '0004_hotelfoodorder_order_stautus_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotelfoodorder',
            name='order_stautus',
        ),
        migrations.RemoveField(
            model_name='hotelfoodorderitems',
            name='order_stautus',
        ),
        migrations.AddField(
            model_name='hoteldrinksorder',
            name='order_status',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Status'),
        ),
        migrations.AddField(
            model_name='hoteldrinksorderitems',
            name='order_status',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Status'),
        ),
        migrations.AddField(
            model_name='hotelfoodorder',
            name='order_status',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Status'),
        ),
        migrations.AddField(
            model_name='hotelfoodorderitems',
            name='order_status',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Status'),
        ),
        migrations.AddField(
            model_name='hotelroomsorder',
            name='order_status',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Status'),
        ),
        migrations.AddField(
            model_name='hotelroomsorderitems',
            name='order_status',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Status'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='is_supervisor',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='myuser',
            name='is_waiter',
            field=models.BooleanField(default=False),
        ),
    ]
