# Generated by Django 3.2.4 on 2021-06-21 13:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210621_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 21, 13, 44, 2, 342549, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='media/videos/'),
        ),
    ]