# Generated by Django 3.2.5 on 2021-08-31 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Shop', '0003_auto_20210830_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cupon_offer',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
    ]