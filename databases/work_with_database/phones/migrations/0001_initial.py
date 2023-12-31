# Generated by Django 3.1.2 on 2023-11-21 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Цена')),
                ('image', models.ImageField(upload_to='', verbose_name='Фото')),
                ('release_date', models.DateTimeField(auto_now=True, verbose_name='Дата релиза')),
                ('lte_exists', models.BooleanField(default=True)),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
        ),
    ]
