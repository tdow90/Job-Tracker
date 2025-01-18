from rest_framework import serializers
from .models import Job

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['title', 'link', 'company', 'location', 'date_posted', 'job_details', 'description']