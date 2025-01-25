from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),  # URL for user registration
    path('', views.profile_view, name='profile_view'),
]