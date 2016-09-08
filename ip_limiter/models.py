from django.db import models


class IpLimiter(models.Model):
    ip = models.CharField(max_length=20)
    visits_count = models.IntegerField()
    outset_time = models.DateTimeField()

    class Meta:
        verbose_name = "Ip控制"