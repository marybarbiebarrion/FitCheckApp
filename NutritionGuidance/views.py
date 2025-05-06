from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from UserProfile.models import User
from .forms import HydrationTrackerForm
from .models import Meal, Meal_Plan, Hydration_Tracker


@login_required(login_url='/')
def ng_homeview(request):
    message = ""
    if request.method == 'POST':
        user = User.objects.get(user_id=request.user.user_id)
        queried_meals = Meal.objects.exclude(allergen_id__allergen_name__contains="Milk").filter(calories__lte=2000/3).order_by('?')[:21]
            # assign them to different meal types (breakfast, lunch, dinner)
        meal_type = ["breakfast", "lunch", "dinner"]
            # assign them to different days of the week
        days = ["sun", "mon", "tue", "wed", "thu", "fri", "sat"]
        
        for i in range(len(days)):
            for j in range(len(meal_type)):
                mealplan = Meal_Plan()
                mealplan.user_id = user
                mealplan.meal_id = queried_meals[i*3 + j]
                mealplan.meal_type = meal_type[j]
                mealplan.day = days[i]
                mealplan.save()

        return redirect('NutritionGuidance:ng_index')
            
    else:
        user = User.objects.get(user_id=request.user.user_id)
        current_meal = Meal_Plan.objects.filter(user_id=user).first()
        ht = Hydration_Tracker.objects.filter(user_id=user).first()
    return render(request, 'index.html', {'current_meal': current_meal, 'ht': ht, 'message': message})

@login_required(login_url="/")
def ht_create(request):
    if request.method == 'POST':
        htform = HydrationTrackerForm(request.POST, prefix='hydrotracker')
        if htform.is_valid():
            ht = Hydration_Tracker()
            ht.user_id = User.objects.get(user_id=request.user.user_id)
            ht.container_size = htform.cleaned_data.get('container_size')
            ht.water_goal = htform.cleaned_data.get('water_goal')
            ht.active_start = htform.cleaned_data.get('active_start')
            ht.active_end = htform.cleaned_data.get('active_end')
            ht.save()
            
            return redirect('NutritionGuidance:ng_index')
    else:
        htform = HydrationTrackerForm(prefix='hydrotracker')
    return render(request, 'ht_form.html', {'form': htform})

class NG_MPListView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        meals = Meal_Plan.objects.filter(user_id=self.request.user)
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
        meal = Meal_Plan.objects.filter(user_id=self.request.user).first()
        meal.delete()
        return redirect('NutritionGuidance:ng_index')

class NG_Recipe(View):
    def get(self, request, meal_id, *args, **kwargs):
        meal = Meal.objects.get(meal_name=meal_id)
        return render(request, 'recipe.html', {'meal': meal})

class HT_Update(View):
    def get(self, request):
        tracker = Hydration_Tracker.objects.get(user_id=self.request.user)
        htform = HydrationTrackerForm(instance=tracker)
        return render(request, 'ht_form.html', {'form': htform})
    
    def post(self, request):
        tracker = Hydration_Tracker.objects.get(user_id=self.request.user)
        htform = HydrationTrackerForm(request.POST, instance=tracker)
        if htform.is_valid():
            htform.save()
            return redirect('NutritionGuidance:ng_index')
        return render(request, 'ht_form.html', {'form': htform})
    
class HT_Delete(View):
    def post(self, request, *args, **kwargs):
        tracker = Hydration_Tracker.objects.get(user_id=self.request.user)
        tracker.delete()
        return redirect('NutritionGuidance:ng_index')
            
        
