# Generated by Django 3.1.3 on 2021-01-01 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_auto_20201231_1030'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='totalprice',
            field=models.IntegerField(default=0),
        ),
    ]
