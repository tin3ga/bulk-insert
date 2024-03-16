# Generated by Django 5.0.3 on 2024-03-16 18:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productvariant',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variants', to='api.product'),
        ),
    ]