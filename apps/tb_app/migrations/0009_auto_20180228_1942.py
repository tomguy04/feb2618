# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-01 03:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tb_app', '0008_auto_20180228_1751'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tripschedule',
            name='user',
        ),
        migrations.AddField(
            model_name='tripschedule',
            name='user_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
