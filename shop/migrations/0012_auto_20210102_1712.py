# Generated by Django 3.1.3 on 2021-01-02 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_order_totalprice'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='cur_status',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='order',
            name='updates',
            field=models.CharField(default='', max_length=5000),
        ),
    ]
