from django.contrib import admin
from django.contrib.auth.models import Group
from django_celery_beat.models import PeriodicTask, ClockedSchedule, CrontabSchedule, IntervalSchedule, SolarSchedule

from scheduler.models import APIScheduler


class APISchedulerAdmin(admin.ModelAdmin):
    """Class to have custom controls on django admin portal"""

    list_display = ('id', 'request_url', 'executable_time', 'status')
    readonly_fields = ('task', 'status')
    list_filter = ('status',)

admin.site.unregister(Group)
admin.site.unregister(PeriodicTask)
admin.site.unregister(ClockedSchedule)
admin.site.unregister(CrontabSchedule)
admin.site.unregister(IntervalSchedule)
admin.site.unregister(SolarSchedule)

admin.site.register(APIScheduler, APISchedulerAdmin)
