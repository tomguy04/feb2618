# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-25 23:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tb_app', '0006_auto_20180225_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='admin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='adminrelated', to='tb_app.User'),
        ),
    ]
