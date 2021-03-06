# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-24 07:41
from __future__ import unicode_literals

import db.AbstractModel
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_auto_20171019_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertise',
            name='create_time',
            field=models.CharField(default=db.AbstractModel.get_time, max_length=50),
        ),
        migrations.AlterField(
            model_name='category',
            name='create_time',
            field=models.CharField(default=db.AbstractModel.get_time, max_length=50),
        ),
        migrations.AlterField(
            model_name='goods_info',
            name='create_time',
            field=models.CharField(default=db.AbstractModel.get_time, max_length=50),
        ),
    ]
