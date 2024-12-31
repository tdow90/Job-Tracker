from django.db import models

# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=100)
    link = models.URLField(max_length=200)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    date_posted = models.DateField(null=True, blank=True)
    job_details = models.TextField(max_length=500)

    class Meta:
        unique_together = ('title', 'company', 'link')

    def __str__(self):
        return self.title