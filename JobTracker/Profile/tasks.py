from celery import shared_task
from .models import Profile
#from JobApi.models import Job
from django.core.mail import send_mail

@shared_task(name="Job Alert Emails")
def job_alert_emails():
    user_profile = Profile.objects.all()
    for profile in user_profile:
        if profile.emailed_job_alerts:
            send_mail(
                "Test Subject",
                "Test message",
                "sent_from@gmail.com",
                ["test@gmail.com"],
                fail_silently=False,
            )







