# Generated by Django 3.1.3 on 2022-10-20 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0008_remove_product_imgfile'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='modify_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]