# Generated by Django 4.1.4 on 2023-02-01 10:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scents', '0009_remove_product_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='womenscent',
            name='product_ptr',
        ),
        migrations.DeleteModel(
            name='MenScent',
        ),
        migrations.DeleteModel(
            name='WomenScent',
        ),
        migrations.CreateModel(
            name='MenScent',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('scents.product',),
        ),
        migrations.CreateModel(
            name='WomenScent',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('scents.product',),
        ),
    ]
