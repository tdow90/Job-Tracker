# **Project Name:** Job Tracker with Alerts  

## **Introduction**  
This is my very first **Django project**, and it's also the very first thing I've hosted online! I'm a beginner backend developer, and I’ve been learning Django and Django Rest Framework (DRF) as part of my journey. This project is a result of that learning, with help from ChatGPT in brainstorming a beginner-friendly idea. My goal was to build a simple yet practical app using the technologies below.

I decided to make this project open-source so anyone can contribute to making it better. Feel free to host it locally, submit a PR, or suggest improvements!

## **Description**  
This is a web application built with **Django** & **Django Rest Framework (DRF)** that scrapes job postings from a job board (currently scraping **CareerBeacon** for jobs in New Brunswick, Canada), stores the data in a database, and sends email notifications to users when new jobs match their preferences.

---

## **Core Features**  

### 1. **Job Scraping**  
- The app uses **BeautifulSoup** to fetch job postings from **CareerBeacon**.  
- Extracts job details such as:  
  - Title  
  - Company  
  - Location  
  - Salary  
  - Job description  

### 2. **Database Integration**  
- Jobs and user preferences are stored in a database.  
- User profiles include job title, location, and keywords, which help tailor the job alerts. Allowing users to opt into job alerts via a checkbox.

### 3. **API Endpoints**  
- Built using DRF, the API allows users to:   
  - View saved job postings via API.

### 4. **Mailer Integration**  
- The app uses **Django’s EmailBackend** to send emails to users when new job matches are found.  
- Users receive weekly alerts for new jobs matching their criteria.  

### 5. **Scheduler**  
- A scheduler (using **APScheduler**) periodically scrapes job postings and checks for new matches.  
- Jobs are fetched on a regular schedule, ensuring users get fresh job alerts.

---

## **Tech Stack**  

- **Django Rest Framework (DRF)**: For building the backend API  
- **MySQL Locally**: For database storage  
- **BeautifulSoup/Scrapy**: For web scraping of job data  
- **Django Mailer**: For email notifications to users  
- **Django Q/Celery/APScheduler**: For task scheduling to scrape jobs and send emails  

---

## **Important Note**  
Site is hosted at: https://job-tracker-t8yd.onrender.com
I decided to host this project on Render's free tier. But the free tier doesn't include background workers. So for now, 
i wont be automatically scraping jobs or deleting them. Plus I won't be able to send emails, the code works locally, 
but I can't set up background workers for free now. I may transition in the future to another hosting service. 

Jobs will be static for now. They wont be updated. 


