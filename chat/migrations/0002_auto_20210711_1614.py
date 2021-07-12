# Generated by Django 3.2.4 on 2021-07-11 10:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='timestamp',
        ),
        migrations.AddField(
            model_name='message',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 11, 10, 29, 11, 533638, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='message',
            name='time',
            field=models.TimeField(default=datetime.datetime(2021, 7, 11, 10, 29, 11, 533638, tzinfo=utc)),
        ),
    ]
