from django.shortcuts import render_to_response
from .forms import Searcher
from captcha.models import CaptchaStore
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied
from ip_limiter.ipLimiter import filter_ip
from django.template import RequestContext
from django.http import JsonResponse


def search_view(request):
    if request.POST:
        try:
            filter_ip(request)
        except:
            raise PermissionDenied
        form = Searcher(request.POST)
        if form.is_valid():
            result = form.exe_query(form.cleaned_data['search'])
        else:
            return HttpResponse('validate error')
    else:
        form = Searcher()
        result = '- -'

    return render_to_response('searchs/index.html',
                              {'form': form, 'result': result},
                              context_instance=RequestContext(request))


def ajax_res(request):
    if request.is_ajax():
        captcha_store = CaptchaStore.objects.filter(
            response=request.GET['response'],
            hashkey=request.GET['hashkey'],
        )
        if captcha_store:
            json_data = {'status': 1}
        else:
            json_data = {'status': 0}
        return JsonResponse(json_data)
    else:
        json_data = {'status': 0}
        return JsonResponse(json_data)