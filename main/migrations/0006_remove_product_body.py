# Generated by Django 3.2.7 on 2022-02-20 08:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_product_body'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='body',
        ),
    ]
