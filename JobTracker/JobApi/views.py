from django.shortcuts import render
from .job_scraper import career_beacon_job_scraper, get_jobs, delete_all_jobs
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from .serializers import JobSerializer 
from .models import Job
from django.utils import timezone
from datetime import timedelta, date
from rest_framework.response import Response


# Create your views here.
def scrape(request):
    get_jobs()
    return HttpResponse("Scraper complete and jobs added to DB.")

def delete_jobs(request):
    delete_all_jobs()
    return HttpResponse("All jobs deleted from DB.")

#List all Jobs in DB
class JobList(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = JobSerializer(queryset, many=True)
        count = queryset.count()
        return Response({
            "count": count,
            "results": serializer.data
            })
    

#List all new jobs(<= 1week)
class NewJobList(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


    def get_queryset(self):
        one_week_ago = timezone.now() - timedelta(days=7)
        return super().get_queryset().filter(date_posted__gte=one_week_ago)

#List all jobs in city
class CityJobList(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
   

    def get_queryset(self):
        city = self.kwargs['city']
        return super().get_queryset().filter(location__icontains=city)

#list all new jobs in a city
class NewCityJobList(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


    def get_queryset(self):
        one_week_ago = timezone.now() - timedelta(days=7)
        city = self.kwargs['city']
        return super().get_queryset().filter(date_posted__gte=one_week_ago, location__icontains=city)

#List all new jobs by type   
class NewJobTypeJobList(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    def get_queryset(self):
        one_week_ago = timezone.now() - timedelta(days=7)
        job_type = self.kwargs['jobType']
        return super().get_queryset().filter(date_posted__gte=one_week_ago, title__icontains=job_type)

#List all jobs by type   
class TitleJobList(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
  

    def get_queryset(self):
        job_type = self.kwargs['jobType']
        return super().get_queryset().filter(title__icontains=job_type)

#List all jobs by type in a specific city  
class CityTitleJobList(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    def get_queryset(self):
        job_type = self.kwargs.get('jobType', '')  # Get jobType from URL
        city = self.kwargs.get('city', '')  # Get city from URL
        return super().get_queryset().filter(
            title__icontains=job_type,
            location__icontains=city  # Use the 'city' field to filter
        )

#List all new jobs by type in a city
class NewCityTitleJobList(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    def get_queryset(self):
        one_week_ago = timezone.now() - timedelta(days=7)
        job_type = self.kwargs.get('jobType', '')  # Get jobType from URL
        city = self.kwargs.get('city', '')  # Get city from URL
        return super().get_queryset().filter(
            date_posted__gte=one_week_ago,
            title__icontains=job_type,
            location__icontains=city  # Use the 'city' field to filter
        )

