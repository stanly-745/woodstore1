# Generated by Django 4.0.4 on 2022-05-15 05:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_remove_bill_product_bill_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='quantity',
        ),
    ]