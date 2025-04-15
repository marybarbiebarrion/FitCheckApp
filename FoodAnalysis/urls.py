from django.urls import path
from .views import food_analysis_view

urlpatterns = [
    path('food_analysis/', food_analysis_view, name='food_analysis'),
]

app_name="FoodAnalysis"