# Generated by Django 4.1.2 on 2022-10-17 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='test'),
            preserve_default=False,
        ),
    ]
