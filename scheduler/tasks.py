import requests

from celery import shared_task

from scheduler.models import APIScheduler


@shared_task(name='scheduled_task')
def scheduled_task(task_id):
    """Function to execute the scheduled task and update the respective status"""

    task = APIScheduler.objects.get(id=task_id)
    try:
        if task.request_type == 'get':
            requests.get(task.request_url, headers=task.request_headers)
        elif task.request_type == 'post':
            requests.post(task.request_url, data=task.request_body, headers=task.request_headers)
        elif task.request_type == 'put':
            requests.put(task.request_url, data=task.request_body, headers=task.request_headers)
        elif task.request_type == 'delete':
            requests.delete(task.request_url, data=task.request_body, headers=task.request_headers)

        task.status = 'done'
        task.save()

        return True
    except Exception:
        task.status = 'failed'
        task.save()

        return False