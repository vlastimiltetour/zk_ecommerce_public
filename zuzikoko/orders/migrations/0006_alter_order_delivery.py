# Generated by Django 4.1.2 on 2023-01-08 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_alter_order_delivery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery',
            field=models.CharField(max_length=50),
        ),
    ]
