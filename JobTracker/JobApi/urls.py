from django.urls import path

from . import views

urlpatterns = [
    path("scrape/", views.scrape, name="scrape"),
    path("jobs/", views.JobList.as_view(), name="jobs"),
    path("new_jobs/", views.NewJobList.as_view(), name="new_jobs"),
    path("<city>/", views.CityJobList.as_view(), name="city_jobs"),
    path("new/<city>/", views.NewCityJobList.as_view(), name="new_city_job_list"),

]