# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Human',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('xh', models.IntegerField(unique_for_date=True, verbose_name='学号')),
                ('name', models.CharField(max_length=70, verbose_name='姓名')),
                ('phoneNumber', models.CharField(max_length=200, verbose_name='电话')),
                ('college', models.CharField(blank=True, max_length=200, verbose_name='学院')),
                ('gender', models.CharField(blank=True, max_length=20, choices=[('male', '男'), ('female', '女')], verbose_name='性别')),
            ],
            options={
                'verbose_name': '联系人',
            },
        ),
    ]
