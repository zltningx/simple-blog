from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, TemplateView
from .query import Query


class SearchIndexView(TemplateView):
    template_name = "searchs/index.html"


class SearchResultView(ListView):
    template_name = "searchs/result.html"
    context_object_name = "search_result"

    def get_context_data(self, **kwargs):
        kwargs['s'] = self.request.GET.get('s', '')
        return super(SearchResultView, self).get_context_data(**kwargs)

    def get_queryset(self):
        result = self.request.GET.get('s', '')
        sql_search_list = Query().query(content=result)
        return sql_search_list