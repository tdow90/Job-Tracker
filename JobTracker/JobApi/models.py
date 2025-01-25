from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField(max_length=300)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    date_posted = models.DateField(null=True, blank=True)
    job_details = models.TextField(max_length=500)
    description = models.TextField(max_length=1000)
    created_date = models.DateTimeField(auto_now_add=True) #Automatically create date when added to the DB

    class Meta:
        unique_together = ('title', 'company', 'link')

    def __str__(self):
        return self.title
    
#Need to create a preference model, this should be one-to-one with the user. Each user should have one preference and vice-verse. 
class Preference(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name="user_profile")
    city = models.CharField(max_length=100, null=True, blank=True)
    job_type = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.user} wants {self.job_type} in {self.city}"