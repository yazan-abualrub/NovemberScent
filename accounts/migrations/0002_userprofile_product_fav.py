# Generated by Django 4.1.4 on 2023-01-15 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scents', '0005_menscent_womenscent'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='product_fav',
            field=models.ManyToManyField(to='scents.product'),
        ),
    ]
