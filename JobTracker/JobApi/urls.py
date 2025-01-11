from django.urls import path

from . import views

urlpatterns = [
    path("scrape/", views.scrape, name="scrape"),
    path('delete/', views.delete_jobs, name="delete_jobs"),
    path("jobs/", views.JobList.as_view(), name="jobs"),
    path("new_jobs/", views.NewJobList.as_view(), name="new_jobs"),
    path("<city>/", views.CityJobList.as_view(), name="city_jobs"),
    path("new/<city>/", views.NewCityJobList.as_view(), name="new_city_job_list"),
    path("title/<jobType>/", views.TitleJobList.as_view(), name="title_jobs"),
    path('title/<str:jobType>/<str:city>/', views.CityTitleJobList.as_view(), name='job_type_city_list'),
    path('title/new/<str:jobType>/<str:city>/', views.NewCityTitleJobList.as_view(), name="new_job_type_city_list"),


]