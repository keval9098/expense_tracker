# Generated by Django 3.0.3 on 2020-02-27 17:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='spent',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 27, 22, 48, 56, 270259)),
        ),
    ]