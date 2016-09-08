from .models import IpLimiter
from django.http import HttpRequest
from django.utils import timezone

MAX_VISITS = 16
MIN_SECONDS = 24 * 60 * 60


def filter_ip(request):
    remote_ip = HttpRequest.get_host(request)

    try:
        record = IpLimiter.objects.get(ip=remote_ip)
    except IpLimiter.DoesNotExist:
        IpLimiter.objects.create(ip=remote_ip,
                                 visits_count=1,
                                 outset_time=timezone.now())
        return

    passed_time = (timezone.now() - record.outset_time).seconds

    if record.visits_count > MAX_VISITS and passed_time < MIN_SECONDS:
        raise Exception('403')
    else:
        if passed_time < MIN_SECONDS:
            record.visits_count += 1
            record.save()
        else:
            record.visits_count = 1
            record.outset_time = timezone.now()
            record.save()