from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('user_create/', views.user_create, name='user_create'),
    path('user_login/', views.user_login, name='user_login'),
    path('health_profile/', views.health_profile, name='health_profile'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.user_logout, name='user_logout'),
]
