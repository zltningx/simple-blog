from django.conf.urls import url
from .views import SearchResultView, SearchIndexView
from django.views.decorators.cache import cache_page


urlpatterns = [
    url(r'^$', cache_page(60 * 15)(SearchIndexView.as_view()), name='index'),
    url(r'^search/$', cache_page(60 * 15)(SearchResultView.as_view()), name='result'),
]