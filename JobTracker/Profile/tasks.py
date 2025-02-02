from celery import shared_task
from .models import Profile
from JobApi.models import Job
from django.core.mail import send_mail
from django.utils import timezone
from datetime import timedelta

@shared_task(name="Job Alert Emails")
def job_alert_emails():
    one_week_ago = timezone.now() - timedelta(days=7)
    user_profile = Profile.objects.all()
    for profile in user_profile:
        if profile.emailed_job_alerts:
            city = profile.city
            user_jobs = Job.objects.filter(date_posted__gte=one_week_ago, location__icontains=city)
            profile_email_address = str(profile.email)
            #start of html
            html_content = """
            <html>
            <body>
                <h1>New Job Listings</h1>
            """

            for job in user_jobs:
                html_content +=f"""
                <div>
                <h2>{job.title}</h2>  
                <p><strong>Location:</strong> {job.location}</p> 
                <p><strong>Details:</strong></p>
                <div>
                    {job.job_details} 
                </div>
                <p><strong>Description:</strong></p>
                <div>
                    {job.description} 
                </div>
                <hr>
                </div>
                """
                #end of html
                html_content += """
                </body>
                </html>
                """

                #Create plain text backup
                plain_text_content = f"New Job Listings:\n\n"

                for job in user_jobs:
                    plain_text_content += f"{job.title}\nLocation: {job.location}\n\n{job.job_details}\n\n---\n"


            send_mail(
                "New Job Alerts",
                plain_text_content,
                "sent_from@gmail.com",
                [profile_email_address],
                html_message=html_content,
            )







