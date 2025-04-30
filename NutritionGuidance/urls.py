from django.urls import path
from .views import ng_homeview, NG_MPListView, NG_MPDemo, NG_NextMeal, NG_Recipe

urlpatterns = [
    path('home/', ng_homeview, name='ng_index'),
    path('meal_plan/', NG_MPListView.as_view(), name='ng_planlist'),
    path('demo/', NG_MPDemo.as_view(), name='ng_plancreate'),
    path('nextmeal/', NG_NextMeal.as_view(), name='ng_nextmeal'),
    path('recipe/<meal_id>', NG_Recipe.as_view(), name='ng_recipe')
]

app_name="NutritionGuidance"