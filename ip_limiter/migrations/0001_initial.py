# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IpLimiter',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('ip', models.CharField(max_length=20)),
                ('visits_count', models.IntegerField()),
                ('outset_time', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'Ip控制',
            },
        ),
    ]
