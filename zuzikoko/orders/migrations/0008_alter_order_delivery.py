# Generated by Django 4.1.2 on 2023-01-09 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_alter_order_delivery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery',
            field=models.CharField(choices=[('Osobně', 'Osobně'), ('Balík', 'Balík')], max_length=100),
        ),
    ]