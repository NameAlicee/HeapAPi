# Generated by Django 3.2.4 on 2021-06-22 05:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210621_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 22, 5, 10, 57, 71821, tzinfo=utc)),
        ),
    ]
