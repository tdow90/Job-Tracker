from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#profile Models
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name="user_profile")
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=254)
    city = models.CharField(max_length=100, null=True, blank=True)
    job_type = models.CharField(max_length=100, null=True, blank=True)
    #T/F field for enabling/disabling job notifications.
    emailed_job_alerts = models.BooleanField(default=False)