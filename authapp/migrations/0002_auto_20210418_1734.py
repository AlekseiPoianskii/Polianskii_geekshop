# Generated by Django 2.2.18 on 2021-04-18 10:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 20, 10, 34, 32, 98606, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='bdate',
            field=models.DateField(default=datetime.datetime(2021, 4, 18, 10, 34, 32, 98606, tzinfo=utc), verbose_name='дата рождения'),
        ),
    ]
