# Generated by Django 3.2.5 on 2021-08-30 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Shop', '0002_category_seller'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='cupon_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='cupon_offer',
            field=models.FloatField(default=1, null=True),
        ),
    ]
