# Generated by Django 3.2.7 on 2021-09-23 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_cartitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='product_price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
