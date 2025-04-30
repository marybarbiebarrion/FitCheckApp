from django.http import HttpResponseRedirect
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from .models import Ingredient, Recipe, Recipe_Ingredients, Meal, Meal_Favorites, Meal_Plan
from UserProfile.models import User
from .forms import MealPlanForm
from django.db.models.query import QuerySet

    
def ng_homeview(request):
    message = ""
    if request.method == 'POST':
        mealform = MealPlanForm(request.POST, prefix='mealplan')
        if mealform.is_valid():
            message = "Successfully generated a meal plan."
            # select 21 random meals
            queried_meals = Meal.objects.exclude(allergen_id__allergen_name__contains="Milk").filter(calories__lte=2000/3).order_by('?')[:21]
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
        current_meal = Meal_Plan.objects.filter(user_id=1).first()
    return render(request, 'index.html', {'current_meal': current_meal, 'form': mealform, 'message': message})

class NG_MPListView(View):
    def get(self, request, *args, **kwargs):
        meals = Meal_Plan.objects.filter(user_id=1)
        days = {
            "sun": "Sunday",
            "mon": "Monday",
            "tue": "Tuesday",
            "wed": "Wednesday",
            "thu": "Thursday",
            "fri": "Friday",
            "sat": "Saturday",
        }
        
        return render(request, 'planlist.html', {'meals': meals, "days": days})
    
class NG_NextMeal(View):
    def post(self, request, *args, **kwargs):
        meal = Meal_Plan.objects.filter(user_id=1).first()
        meal.delete()
        return redirect('NutritionGuidance:ng_index')

class NG_Recipe(View):
    def get(self, request, meal_id, *args, **kwargs):
        meal = Meal.objects.get(meal_name=meal_id)
        return render(request, 'recipe.html', {'meal': meal})

class NG_MPDemo(View):
    def get(self, request, *args, **kwargs):
        meals = Meal.objects.exclude(allergen_id__allergen_name__contains="Sesame").filter(calories__lte=2000/3).order_by('?')[:21]
        return render(request, 'demo.html', {'meals': meals})
    
