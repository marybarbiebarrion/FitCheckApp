from django.urls import path
from .views import ng_homeview, ht_create, NG_MPListView, NG_NextMeal, NG_Recipe, HT_Update, HT_Delete

urlpatterns = [
    path('home/', ng_homeview, name='ng_index'),
    path('meal_plan/', NG_MPListView.as_view(), name='ng_planlist'),
    path('nextmeal/', NG_NextMeal.as_view(), name='ng_nextmeal'),
    path('recipe/<meal_id>', NG_Recipe.as_view(), name='ng_recipe'),
    path('hydrotrack/', ht_create, name='ht_create'),
    path('hydrotrack/settings', HT_Update.as_view(), name='ht_update'),
    path('hydrotrack/disable', HT_Delete.as_view(), name='ht_delete')
]

app_name="NutritionGuidance"