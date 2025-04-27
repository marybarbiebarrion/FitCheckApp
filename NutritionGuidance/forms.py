from django import forms

from .models import Meal, Meal_Plan

class MealPlanForm(forms.ModelForm):
    class Meta:
        model = Meal_Plan
        fields = ['user_id']
        widgets = {
            'user_id': forms.Select(attrs={'placeholder': 'Select user'})
        }