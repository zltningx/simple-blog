from django.conf.urls import url
from . import views
from .feeds import LastestPostFeed
from django.views.decorators.cache import cache_page

urlpatterns = [
    # post views
    url(r'^$', views.post_list, name='post_list'),
    # url(r'^$', views.PostListView.as_view(), name='post_list'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$',
        views.post_detail, name='post_detail'),
    url(r'^(?P<post_id>\d+)/share/$', views.post_share, name='post_share'),
    url(r'^tag/(?P<tag_slug>[-\w]+)/$', views.post_list,
        name='post_list_by_tag'),
    url(r'^feed/$', LastestPostFeed(), name='post_feed'),
    url(r'^search/$', cache_page(60 * 15)(views.SearchView.as_view()), name='post_search'),
    url(r'^my_blog/$', cache_page(60 * 15)(views.PostMyselfView.as_view()), name='post_myself'),
]