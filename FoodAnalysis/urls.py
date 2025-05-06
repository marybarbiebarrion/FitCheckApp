from django.urls import path
from .views import food_analysis_view, food_analysis_detail_view

urlpatterns = [
    path('food_analysis/', food_analysis_view, name='food_analysis'),
    path('food_analysis/<int:pk>/', food_analysis_detail_view, name='food_analysis_detail'),
]

app_name = "FoodAnalysis"