release: python manage.py migrate --no-input

web: gunicorn dynamic_scheduler.wsgi
celery_worker: celery -A dynamic_scheduler worker --beat --scheduler django --loglevel=info
