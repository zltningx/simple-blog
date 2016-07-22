from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatechars, slice_filter
from .models import Post


class LastestPostFeed(Feed):
    title = '一只攻城狮'
    link = '/blog/'
    description = '关注网络安全|娱乐圈|Python|Linux'

    def items(self):
        return Post.published.all()[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return slice_filter(item.body, '50')

    # def item_link(self, item):
    #     return item.get_absolute_url()