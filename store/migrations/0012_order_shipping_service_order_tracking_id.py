# Generated by Django 4.2 on 2024-09-18 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_alter_order_options_alter_orderitem_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='shipping_service',
            field=models.CharField(blank=True, choices=[('DHL', 'DHL'), ('FedX', 'FedX'), ('UPS', 'UPS'), ('GIG Logistics', 'GIG Logistics')], default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='tracking_id',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
    ]
