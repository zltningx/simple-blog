from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class PublishManager(models.Manager):
    """查询数据库manager
    """
    def get_queryset(self):
        return super(PublishManager, self).get_queryset().filter(
            status='published'
        )


class Post(models.Model):
    STATUS_CHOICE = (
        ('draft', '草稿'),
        ('published', '发布')
    )
    OWNER_CHOICE = (
        ('myself', '原创'),
        ('others', '转载')
    )
    title = models.CharField(max_length=250, verbose_name='标题')
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, related_name='blog_posts',
                               verbose_name='作者')
    body = RichTextUploadingField(verbose_name='正文')
    publish = models.DateTimeField(default=timezone.now, verbose_name='发布时间')
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICE,
                              default='draft',
                              verbose_name='发布状态')
    owner = models.CharField(max_length=10,
                             choices=OWNER_CHOICE,
                             default='myself',
                             verbose_name='原创/转载')

    object = models.Manager()
    published = PublishManager()
    tags = TaggableManager()

    def get_absolute_url(self):
        # 返回 view.detail 需要的url参数
        return reverse('blog:post_detail',
                       args=[self.publish.year,
                             self.publish.strftime('%m'),
                             self.publish.strftime('%d'),
                             self.slug])

    class Meta:
        ordering = ('-publish',)
        verbose_name = "博文"

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', verbose_name='评论')
    name = models.CharField(max_length=80, verbose_name='姓名')
    email = models.EmailField(verbose_name='邮箱')
    body = models.TextField(verbose_name='内容')
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created', )
        verbose_name = "评论"

    def __str__(self):
        return "评论 {} By： {}".format(self.post, self.name)
