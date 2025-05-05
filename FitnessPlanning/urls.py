from django.urls import path
from .views import fitness_planning_dashboard
urlpatterns = [
path('fitness/', fitness_planning_dashboard, name='fitness_planning_dashboard'),
]

app_name = "FitnessPlanning"