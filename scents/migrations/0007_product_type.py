# Generated by Django 4.1.4 on 2023-01-31 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scents', '0006_product_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='type',
            field=models.CharField(default='men', max_length=6),
        ),
    ]
