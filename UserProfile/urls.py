from django.urls import path
from . import views

urlpatterns = [
    path('', views.splash, name='home'),
    path('splash/', views.splash, name='splash'),
    path('user_create/', views.user_create, name='user_create'),
    path('user_login/', views.user_login, name='user_login'),
    path('health_profile/', views.health_profile, name='health_profile'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_view, name='user_logout'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
]

app_name="UserProfile"