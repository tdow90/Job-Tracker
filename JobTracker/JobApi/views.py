from django.shortcuts import render
from .job_scraper import career_beacon_job_scraper, get_jobs
from django.http import HttpResponse

# Create your views here.
def scrape(request):
    get_jobs()
    return HttpResponse("Scraper complete and jobs added to DB.")


