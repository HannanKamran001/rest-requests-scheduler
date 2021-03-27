from django.db import models
from django.db.models import JSONField
from django_celery_beat.models import PeriodicTask, ClockedSchedule

from scheduler.constants import REQUEST_TYPE_CHOICES, STATUS_CHOICES


class APIScheduler(models.Model):
    """Model class for specifying and scheduling a new request"""

    task = models.OneToOneField(PeriodicTask, null=True, blank=True, on_delete=models.CASCADE)
    request_url = models.CharField(max_length=100, blank=False, null=False)
    request_type = models.CharField(max_length=6, choices=REQUEST_TYPE_CHOICES, default='get')
    request_headers = JSONField(default=dict, null=True, blank=True)
    request_body = JSONField(default=dict, null=True, blank=True)
    executable_time = models.DateTimeField()
    status = models.CharField(max_length=7, choices=STATUS_CHOICES, default='pending')
