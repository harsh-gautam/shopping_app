# Generated by Django 3.1.3 on 2020-12-12 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20201212_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_desc',
            field=models.CharField(max_length=2000),
        ),
    ]