# Generated by Django 3.1.3 on 2022-10-20 05:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0007_product_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='imgfile',
        ),
    ]
