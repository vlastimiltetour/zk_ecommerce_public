# Generated by Django 4.1.2 on 2022-10-19 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_remove_subscribed_email'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subscribed',
            options={'ordering': ['email']},
        ),
        migrations.RemoveIndex(
            model_name='subscribed',
            name='shop_subscr_name_2c4ae3_idx',
        ),
        migrations.RemoveField(
            model_name='subscribed',
            name='name',
        ),
        migrations.AddField(
            model_name='subscribed',
            name='email',
            field=models.EmailField(default=1, max_length=100, unique=True),
            preserve_default=False,
        ),
        migrations.AddIndex(
            model_name='subscribed',
            index=models.Index(fields=['email'], name='shop_subscr_email_b3983a_idx'),
        ),
    ]