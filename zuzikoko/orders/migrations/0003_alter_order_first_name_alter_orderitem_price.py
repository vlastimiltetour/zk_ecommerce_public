# Generated by Django 4.1.2 on 2022-10-19 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order_stripe_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='first_name',
            field=models.CharField(max_length=50, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='price',
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
    ]
