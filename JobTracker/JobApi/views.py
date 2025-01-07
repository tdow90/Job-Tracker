from django.shortcuts import render
from .job_scraper import career_beacon_job_scraper, get_jobs
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from .serializers import JobSerializer 
from .models import Job
from django.utils import timezone
from datetime import timedelta


# Create your views here.
def scrape(request):
    get_jobs()
    return HttpResponse("Scraper complete and jobs added to DB.")


class JobList(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsAdminUser]

class NewJobList(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        one_week_ago = timezone.now() - timedelta(days=7)
        return super().get_queryset().filter(date_posted__gte=one_week_ago)
    
class CityJobList(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        city = self.kwargs['city']
        return super().get_queryset().filter(location__icontains=city)
    
class NewCityJobList(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        one_week_ago = timezone.now() - timedelta(days=7)
        city = self.kwargs['city']
        return super().get_queryset().filter(date_posted__gte=one_week_ago, location__icontains=city)