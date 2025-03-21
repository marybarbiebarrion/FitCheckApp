from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Root route for the home page
    path('user_create/', views.user_create, name='user_create'),  # User registration page
    path('user_login/', views.user_login, name='user_login'),  # User login page
    path('health_profile/', views.health_profile, name='health_profile'),  # Health profile setup page
    path('dashboard/', views.dashboard, name='dashboard'),  # Dashboard page
    path('logout/', views.user_logout, name='user_logout'),  # User logout page
]
