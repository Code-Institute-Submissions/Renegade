# Generated by Django 3.2 on 2022-09-21 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_shippingaddress_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shippingaddress',
            options={'verbose_name_plural': 'Shipping Addresses'},
        ),
    ]