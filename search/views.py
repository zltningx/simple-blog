from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, TemplateView
from django.db.models import Q
from .models import Human
from ratelimit.mixins import RatelimitMixin


class SearchIndexView(TemplateView):
    template_name = "searchs/index.html"


class SearchResultView(RatelimitMixin, ListView):
    template_name = "searchs/result.html"
    context_object_name = "search_list"
    ratelimit_key = 'ip'
    ratelimit_rate = '3/d'
    ratelimit_block = True

    def get_context_data(self, **kwargs):
        kwargs['s'] = self.request.GET.get('s', '')
        return super(SearchResultView, self).get_context_data(**kwargs)

    def get_queryset(self):
        result = self.request.GET.get('s', '')
        result = result.replace("'", "")
        try:
            sql_search_list = Human.object.only(
                'xh', 'name',
            ).filter(
                Q(name__contains=result) |
                Q(xh=result),
            )
        except:
            sql_search_list = Human.object.only(
                'name',
            ).filter(
                Q(name__contains=result),
            )
        return sql_search_list