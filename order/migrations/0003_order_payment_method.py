# Generated by Django 4.1.2 on 2023-08-21 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_cart_color_cart_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment_method',
            field=models.CharField(choices=[('Cash on Delivery', 'Cash on Delivery'), ('PayPal', 'PayPal'), ('SSLcommerz', 'SSLcommerz')], default='Cash on Delivery', max_length=30),
        ),
    ]
