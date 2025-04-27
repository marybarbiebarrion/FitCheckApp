from django.urls import path
from .views import ng_homeview, NG_HomeView, NG_MPListView

urlpatterns = [
    path('home/', ng_homeview, name='ng_index'),
    path('meal_plan/', NG_MPListView.as_view(), name='ng_planlist'),
    # path('create/', mealplan_create, name='ng_plancreate')
]

app_name="NutritionGuidance"