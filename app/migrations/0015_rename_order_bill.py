# Generated by Django 4.0.4 on 2022-06-12 03:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_order_stock_worker_delete_bill'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Order',
            new_name='Bill',
        ),
    ]
