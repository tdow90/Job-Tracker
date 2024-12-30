# **Project Name:** Job Tracker with Alerts  

## **Description**  
Build an application using **Django Rest Framework (DRF)** that scrapes job postings from a job board (e.g., Indeed, LinkedIn, or similar), stores the data in a database, and sends email notifications to users when new jobs match their preferences.  

---

## **Core Features**  

### 1. **Job Scraping**  
- Use a web scraping library like **BeautifulSoup** or **Scrapy** to fetch job postings from a chosen website.  
- Extract job details, such as:  
  - Title  
  - Company  
  - Location  
  - Salary  
  - Job description  

### 2. **Database Integration**  
- Use **Django’s ORM** with a database like PostgreSQL or SQLite to store:  
  - Job postings  
  - User preferences (e.g., keywords, location, job type)  

### 3. **API Endpoints**  
- Build DRF endpoints to allow users to:  
  - Register and manage their accounts.  
  - Set job preferences (e.g., "Python Developer," "Remote").  
  - View saved job postings.  

### 4. **Mailer Integration**  
- Set up a mailer using Django’s **EmailBackend** or a library like **smtplib** or **SendGrid**.  
- Notify users when new jobs matching their preferences are found.  

### 5. **Scheduler**  
- Use a task scheduler like **Django Q**, **Celery**, or **APScheduler** to periodically scrape job postings and check for new matches.  

---

## **Optional Add-Ons for Extra Practice**  

### 1. **Authentication**  
- Add user authentication using Django’s built-in auth system or **Simple JWT** for token-based authentication.  

### 2. **Admin Panel**  
- Leverage Django’s built-in admin panel to view and manage users, jobs, and preferences.  

### 3. **Pagination and Filtering**  
- Use DRF’s **pagination** and **filtering** capabilities to allow users to browse jobs with filters for salary range, location, and job type.  

### 4. **WebSocket Notifications**  
- Use **Django Channels** to provide real-time notifications for new job matches.  

### 5. **Cloud Deployment**  
- Deploy the app on a cloud platform like **AWS**, **Azure**, or **Heroku** for hands-on deployment experience.  

---

## **Tech Stack**  

- **Django Rest Framework (DRF)**: Backend API  
- **PostgreSQL/SQLite**: Database  
- **BeautifulSoup/Scrapy**: Web Scraping  
- **SendGrid/SMTP**: Email Integration  
- **Django Q/Celery/APScheduler**: Task Scheduling  
