# Generated by Django 5.0.7 on 2024-07-25 02:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='creation_date',
            field=models.DateField(default=datetime.datetime(2024, 7, 24, 21, 50, 2, 415912), verbose_name='fecha_creacion'),
        ),
    ]
