# Generated by Django 5.0.7 on 2024-08-08 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0004_remove_item_supplier_item_created_at_item_suppliers_and_more'),
        ('suppliers', '0003_supplier_created_at_supplier_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_photo',
            field=models.ImageField(blank=True, default='', null=True, upload_to='', verbose_name='Product Photo'),
        ),
        migrations.AlterField(
            model_name='item',
            name='suppliers',
            field=models.ManyToManyField(to='suppliers.supplier'),
        ),
    ]