# simple-blog
This just a simple blog write by django


# 更新

  - 2016-07-30 去除了自己写的评论系统，添加了多说!
  - 2016-07-29 增加了search app
  - 2016-07-24 将site部署apache2


# 概述

网站基于Django 1.8.x 开发，集成了多个django 插件
  - ckeditor 富文本编辑器
  - taggit 标签
  - solr 搜索引擎 需要下载 solr 4.10.4 版本 并配置好

安装必要库。
```sh
$ pip install -r path/requirements.txt  
```
创建超级用户
```sh
$ python mannage.py createsuperuser
```
初始化
```sh
$ python mannage.py makemigrations
$ pyhton mannage.py migrate
```
运行
```sh
$ python mannage.py runserver
```

在 simple_project/setting.py
line: 132
更改邮箱账户密码

你还可以部署网站
 - Apache:  http://www.ziqiangxuetang.com/django/django-deploy.html
 - Nginx:   http://www.ziqiangxuetang.com/django/django-nginx-deploy.html
