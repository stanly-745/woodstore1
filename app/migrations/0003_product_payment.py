# Generated by Django 4.0.4 on 2022-05-13 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_product_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='payment',
            field=models.CharField(choices=[('Paid', 'Paid'), ('Pending', 'Pending')], max_length=200, null=True),
        ),
    ]