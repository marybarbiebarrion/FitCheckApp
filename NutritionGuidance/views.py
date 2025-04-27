from django.http import HttpResponse
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from .models import Ingredient, Recipe, Recipe_Ingredients, Meal, Meal_Favorites, Meal_Plan
from UserProfile.models import User
from .forms import MealPlanForm
from django.db.models.query import QuerySet

class NG_HomeView(View):
    def get(self, request, *args, **kwargs):
        meals = Meal.objects.all()
        return render(request, 'index.html', {'meals': meals})

class NG_MPListView(View):
    def get(self, request, *args, **kwargs):
        meals = Meal.objects.filter(user_id=self.user_id)
        return render(request, 'planlist.html', {'meals': meals})
    
def ng_homeview(request):
    if request.method == 'POST':
        mealform = MealPlanForm(request.POST, prefix='mealplan')
        if mealform.is_valid():
            # select 21 random meals
            queried_meals = Meal.objects.order_by('?')[:21]
            # assign them to different meal types (breakfast, lunch, dinner)
            meal_type = ["breakfast", "lunch", "dinner"]
            # assign them to different days of the week
            days = ["sun", "mon", "tue", "wed", "thu", "fri", "sat"]
            
            for i in range(len(days)):
                for j in range(len(meal_type)):
                    mealplan = Meal_Plan()
                    mealplan.user_id = mealform.cleaned_data.get('user_id')
                    mealplan.meal_id = queried_meals[i*3 + j]
                    mealplan.meal_type = meal_type[j]
                    mealplan.day = days[i]
                    mealplan.save()
            return redirect('NutritionGuidance:ng_index')
    else:
        mealform = MealPlanForm(prefix='mealplan')
    return render(request, 'index.html', {'meals': Meal.objects.all(), 'form': mealform})