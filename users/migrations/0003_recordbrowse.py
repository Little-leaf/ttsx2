# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-20 07:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_auto_20171019_1414'),
        ('users', '0002_user_user_recv'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecordBrowse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('set_time', models.DateTimeField(auto_now=True)),
                ('is_delete', models.BooleanField(default=False)),
                ('browse_goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.goods_info')),
                ('browse_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.User')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
