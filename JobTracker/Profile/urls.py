from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),  # URL for user registration
    path('profile/', views.profile_view, name='profile_view'),
    path('', views.about, name='about')
]