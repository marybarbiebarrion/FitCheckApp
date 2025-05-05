from django import forms

from .models import Meal, Meal_Plan, Hydration_Tracker

class MealPlanForm(forms.ModelForm):
    class Meta:
        model = Meal_Plan
        fields = ['user_id']
        widgets = {
            'user_id': forms.Select(attrs={'placeholder': 'Select user'})
        }

class HydrationTrackerForm(forms.ModelForm):
    class Meta:
        model = Hydration_Tracker
        fields = ['user_id', 'container_size', 'water_goal', 'active_start', 'active_end']
        widgets = {
            'user_id': forms.Select(attrs={'placeholder': 'Select user'}),
            'container_size': forms.NumberInput(attrs={'placeholder': 'Input container size (mL): '}),
            'water_goal': forms.NumberInput(attrs={'placeholder': 'Input daily water goal (mL): '}),
            'active_start': forms.TimeInput(attrs={'placeholder': 'Input start of day (ex. 0:00): '}),
            'active_start': forms.TimeInput(attrs={'placeholder': 'Input end of day (ex. 23:59): '})
        }