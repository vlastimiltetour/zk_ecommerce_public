# Generated by Django 4.1.2 on 2022-11-07 19:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0016_product_cz_price_cs_product_cz_price_en'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='cz_price_cs',
        ),
        migrations.RemoveField(
            model_name='product',
            name='cz_price_en',
        ),
    ]
