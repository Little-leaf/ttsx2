# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-19 11:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('set_time', models.DateTimeField(auto_now=True)),
                ('is_delete', models.BooleanField(default=False)),
                ('cag_name', models.CharField(max_length=30)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='goods_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('set_time', models.DateTimeField(auto_now=True)),
                ('is_delete', models.BooleanField(default=False)),
                ('goods_name', models.CharField(max_length=50)),
                ('goods_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('goods_image', models.ImageField(upload_to='')),
                ('goods_short', tinymce.models.HTMLField()),
                ('goods_desc', models.CharField(max_length=1000)),
                ('goods_status', models.BooleanField(default=True)),
                ('goods_unit', models.CharField(max_length=10)),
                ('goods_visits', models.IntegerField(default=0)),
                ('goods_sales', models.IntegerField(default=0)),
                ('goods_cag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.Category')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
