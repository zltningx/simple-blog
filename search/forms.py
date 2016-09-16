from django import forms
from captcha.fields import CaptchaField
from django.db.models import Q
from .models import Human


class Searcher(forms.Form):
    search = forms.CharField(max_length=25,
                           widget=forms.TextInput(
                               attrs={'class': 'form-control',
                                      'placeholder': 'What Do You Wanna?',
                                      'style': 'width: 640px'}))
    captcha = CaptchaField()

    def exe_query(self, result):
        result = result.replace("'", "")
        if result is None:
            return None
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
        if len(sql_search_list) > 100:
            sql_search_list = None
        return sql_search_list