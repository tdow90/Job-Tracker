import requests
from bs4 import BeautifulSoup
import datetime
from .models import Job
from django.db import IntegrityError
from datetime import timedelta, date
from celery import shared_task

#Helper function to get jobs description
def get_job_decription(link, headers):
    detail_url = link
    r = requests.get(detail_url, headers)
    detail_soup = BeautifulSoup(r.content, 'html.parser')
    try:
        description = str(detail_soup.find('section', class_='job_details_container'))
    except:
        description = 'No description included'
    return description

#Function to scrape a specific page in carreer beacon
@shared_task
def career_beacon_job_scraper(page):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.2 Safari/605.1.15'}
    url = f'https://www.careerbeacon.com/en/search/jobs-in-New-Brunswick?page={page}&jvk=2130348'
    r = requests.get(url, headers)
   
    soup  = BeautifulSoup(r.content, 'html.parser')
    divs = soup.find_all('div', class_='non_featured_job_container')

    for item in divs:
        title = item.find('div', class_='serp_job_title h6 text-primary clickable').text.strip()
        link = item.find('a', class_='serp_job_title d-none')['href']
        company = item.find('span', class_='name fw-semibold text-muted').text.strip()
        location = item.find('span', class_='location text-muted').text.strip()

        try:
            date_posted_str = item.find('div', class_='smaller text-muted')['title']
        except:
            date_posted_str = datetime.datetime.today().strftime('%Y-%m-%d')
        try:
            job_details = str(item.find('div', class_='badge badge-primary small px-2 py-1 me-2 mb-2'))
        except:
            job_details = ''
        date_posted = datetime.datetime.strptime(date_posted_str, "%Y-%m-%d").date()
        description = get_job_decription(link, headers)

        try:
            Job.objects.create(
            title = title, 
            link = link,
            company = company,
            location = location,
            date_posted = date_posted, 
            job_details = job_details,
            description = description,
            )
        except IntegrityError as e:
            # Log the error for debugging or potential deduplication strategies
            print(f"Error creating job: {e}")

    return 


@shared_task(name="get_jobs")
def get_jobs():
    print('scrape function called')
    for i in range(20):
        career_beacon_job_scraper(i)

@shared_task(name="delete_jobs")
def delete_all_jobs():
    print("Deleting jobs function called!")
    three_months_ago = date.today() - timedelta(days=1)
    jobs = Job.objects.all()
    for job in jobs:
        if job.date_posted <= three_months_ago:
            job.delete()
            print(f'deleting {job.title} created on {job.date_posted}')


