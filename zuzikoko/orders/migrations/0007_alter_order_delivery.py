# Generated by Django 4.1.2 on 2023-01-09 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_alter_order_delivery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery',
            field=models.CharField(choices=[('Osobní', 'Osobní'), ('vyzvednutí', 'Vyzvednutí')], max_length=100),
        ),
    ]
