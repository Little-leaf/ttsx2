# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-24 07:41
from __future__ import unicode_literals

import db.AbstractModel
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='create_time',
            field=models.CharField(default=db.AbstractModel.get_time, max_length=50),
        ),
    ]
