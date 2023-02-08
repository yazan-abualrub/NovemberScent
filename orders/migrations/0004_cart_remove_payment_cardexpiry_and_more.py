# Generated by Django 4.1.4 on 2023-01-31 11:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scents', '0006_product_size'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0003_rename_shipmentaddress_payment_shipaddress_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='payment',
            name='CardExpiry',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='CardNumber',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='SecurityCode',
        ),
        migrations.CreateModel(
            name='CartDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('quantity', models.IntegerField()),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scents.product')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='details',
            field=models.ManyToManyField(through='orders.CartDetails', to='scents.product'),
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]