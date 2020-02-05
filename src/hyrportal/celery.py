import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hyrportal.settings')

app = Celery('hyrportal')
app.config_from_object('hyrportal.celeryconfig', namespace='CELERY')
app.autodiscover_tasks()