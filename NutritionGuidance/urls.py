from django.urls import path
from .views import nutrition_guidance

urlpatterns = [
    path('home/', nutrition_guidance, name='nutrition_guidance'),
]

app_name="NutritionGuidance"