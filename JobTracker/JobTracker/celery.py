import os
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'JobTracker.settings')  # Ensure correct project name

app = Celery('JobTracker')  # Ensure this matches your project folder name

# Load task modules from all registered Django apps.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Auto-discover tasks in Django apps
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')