from django.urls import path
from . import views

app_name = 'wellnesstracker'  # <-- This is the key line

urlpatterns = [
    path('bmi/', views.bmi_form, name='bmi_form'),
    path('mood/', views.mood_form, name='mood_form'),
    path('sleep/', views.sleep_form, name='sleep_form'),
    path('past-analyses/', views.past_analyses, name='past_analyses'),
]
