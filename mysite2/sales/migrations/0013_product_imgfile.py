# Generated by Django 3.1.3 on 2022-10-20 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0012_remove_product_imgfile'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='imgfile',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
