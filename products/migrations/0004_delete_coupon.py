# Generated by Django 5.0.3 on 2024-04-02 09:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_coupon'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Coupon',
        ),
    ]
