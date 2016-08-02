# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import taggit.managers
import ckeditor_uploader.fields
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0002_auto_20150616_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='姓名')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('body', models.TextField(verbose_name='内容')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ('created',),
                'verbose_name': '评论',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='标题')),
                ('slug', models.SlugField(max_length=250, unique_for_date='publish')),
                ('body', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='正文')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now, verbose_name='发布时间')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('status', models.CharField(default='draft', max_length=10, choices=[('draft', '草稿'), ('published', '发布')], verbose_name='发布状态')),
                ('owner', models.CharField(default='myself', max_length=10, choices=[('myself', '原创'), ('others', '转载')], verbose_name='原创/转载')),
                ('author', models.ForeignKey(verbose_name='作者', related_name='blog_posts', to=settings.AUTH_USER_MODEL)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'ordering': ('-publish',),
                'verbose_name': '博文',
            },
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(verbose_name='评论', related_name='comments', to='blog.Post'),
        ),
    ]
