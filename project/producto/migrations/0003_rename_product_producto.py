# Generated by Django 5.0 on 2023-12-22 23:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0002_rename_name_product_categoria_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product',
            new_name='Producto',
        ),
    ]
