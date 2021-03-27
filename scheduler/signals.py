import json

from django.dispatch import receiver
from django.utils import timezone
from django.db.models.signals import post_save
from django_celery_beat.models import PeriodicTask, ClockedSchedule


from scheduler.models import APIScheduler


@receiver(post_save, sender=APIScheduler)
def create_periodic_task(sender, instance, created, **kwargs):
    """Function to create and schedule a periodic task upon adding a new entry in APIScheduler model"""

    if created:
        instance.task = PeriodicTask.objects.create(
            name=str(timezone.now()),
            start_time=instance.executable_time,
            task='scheduled_task',
            args=json.dumps([instance.id]),
            one_off=True,
            clocked=ClockedSchedule.objects.create(clocked_time=instance.executable_time)
        )
        instance.save()
