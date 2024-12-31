import requests
from bs4 import BeautifulSoup
import datetime
from .models import Job
from django.db import IntegrityError


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
            job_details = item.find('div', class_='badge badge-primary small px-2 py-1 me-2 mb-2').text.split("/")[0].strip()
        except:
            job_details = ''
        date_posted = datetime.datetime.strptime(date_posted_str, "%Y-%m-%d").date()

        try:
            Job.objects.create(
            title = title, 
            link = link,
            company = company,
            location = location,
            date_posted = date_posted, 
            job_details = job_details
            )
        except IntegrityError as e:
            # Log the error for debugging or potential deduplication strategies
            print(f"Error creating job: {e}")

       
    return 

def get_jobs():
    for i in range(40):
        career_beacon_job_scraper(i)
    return



