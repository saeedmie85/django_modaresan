# Generated by Django 4.2 on 2023-06-11 16:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='spacial_user',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 11, 16, 0, 2, 198568, tzinfo=datetime.timezone.utc), verbose_name='تاریخ انقضای اشتراک ویژه'),
        ),
    ]
