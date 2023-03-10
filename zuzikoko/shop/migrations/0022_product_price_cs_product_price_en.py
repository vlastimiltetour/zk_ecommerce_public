# Generated by Django 4.1.2 on 2022-11-08 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0021_remove_product_eur_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price_cs',
            field=models.DecimalField(decimal_places=0, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='price_en',
            field=models.DecimalField(decimal_places=0, max_digits=10, null=True),
        ),
    ]
