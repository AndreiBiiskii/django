# Generated by Django 3.1.2 on 2023-11-21 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Цена'),
        ),
    ]
