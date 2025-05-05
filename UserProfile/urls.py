from django.urls import path
from . import views

urlpatterns = [
    path('', views.splash, name='home'),  # Home or Splash page
    path('splash/', views.splash, name='splash'),  # Splash page for initial load
    path('user_create/', views.user_create, name='user_create'),  # User registration
    path('user_login/', views.user_login, name='user_login'),  # Login page
    path('health_profile/', views.health_profile, name='health_profile'),  # Health Profile page
    path('dashboard/', views.dashboard, name='dashboard'),  # Dashboard page
    path('logout/', views.logout_view, name='user_logout'),  # Logout functionality
    path('edit_profile/', views.edit_profile, name='edit_profile'),  # Edit user profile
]
