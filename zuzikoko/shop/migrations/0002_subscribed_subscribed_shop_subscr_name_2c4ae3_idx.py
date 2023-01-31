# Generated by Django 4.1.2 on 2022-10-19 20:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscribed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date created')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddIndex(
            model_name='subscribed',
            index=models.Index(fields=['name'], name='shop_subscr_name_2c4ae3_idx'),
        ),
    ]