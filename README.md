# simple-blog
This just a simple blog write by django

# 样例

[my simple blog](http://zltningx.com.cn)

# 更新

  - 2016-08-07 为search app 增加了ip访问限制，每天允许访问6次，防止遍历。
  - 2016-08-07 solr 引擎于昨日的服务器（1M & 1G）的dos测试中占用巨而资源，现已移除
  - 2016-08-02 将数据库入库并更新了search app
  - 2016-08-01 采用多数据库联用（sqlite3 + mysql)
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
