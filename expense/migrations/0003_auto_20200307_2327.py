# Generated by Django 3.0.3 on 2020-03-07 17:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0002_spent_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spent',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 7, 23, 27, 24, 911819)),
        ),
    ]
