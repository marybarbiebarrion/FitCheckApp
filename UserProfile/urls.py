from django.urls import path
from . import views

urlpatterns = [
    path('user_create/', views.user_create, name='user_create'),  # User registration page
    path('health_profile/', views.health_profile, name='health_profile'),  # Health profile setup page
    path('dashboard/', views.dashboard, name='dashboard'),  # Dashboard page
]
