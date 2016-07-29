from django.conf.urls import url
from .views import SearchResultView, SearchIndexView


urlpatterns = [
    url(r'^$', SearchIndexView.as_view(), name='index'),
    url(r'^search/$', SearchResultView.as_view(), name='result'),
]