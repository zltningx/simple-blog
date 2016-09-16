from django.conf.urls import url
from .views import search_view, ajax_res


urlpatterns = [
    url(r'^$', search_view, name='index'),
    url(r'^ajax_res/', ajax_res, name='ajax_res'),
]