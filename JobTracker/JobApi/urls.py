from django.urls import path
from . import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="JobTracker API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@yourapi.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],

)

urlpatterns = [
    path("jobs/", views.JobList.as_view(), name="jobs"),
    path("new_jobs/", views.NewJobList.as_view(), name="new_jobs"),
    path("<city>/", views.CityJobList.as_view(), name="city_jobs"),
    path("new/<city>/", views.NewCityJobList.as_view(), name="new_city_job_list"),
    path("title/<jobType>/", views.TitleJobList.as_view(), name="title_jobs"),
    path('title/<str:jobType>/<str:city>/', views.CityTitleJobList.as_view(), name='job_type_city_list'),
    path('title/new/<str:jobType>/<str:city>/', views.NewCityTitleJobList.as_view(), name="new_job_type_city_list"),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]