# Generated by Django 5.0.7 on 2024-08-07 23:46

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0002_alter_supplier_address_alter_supplier_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplier',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='supplier',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]