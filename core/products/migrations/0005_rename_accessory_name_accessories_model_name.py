# Generated by Django 4.2.4 on 2023-08-09 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_accessories_discount_alter_accessories_stock_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accessories',
            old_name='accessory_name',
            new_name='model_name',
        ),
    ]