# Generated by Django 4.2.4 on 2023-08-15 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_alter_menproducts_approved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accessories',
            name='approved',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Disapproved', 'Disapproved')], default='Pending', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='approved',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Disapproved', 'Disapproved')], default='Pending', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='kidproducts',
            name='approved',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Disapproved', 'Disapproved')], default='Pending', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='womanproducts',
            name='approved',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Disapproved', 'Disapproved')], default='Pending', max_length=50, null=True),
        ),
    ]