from django import forms

from .models import Meal, Meal_Plan, Hydration_Tracker

class HydrationTrackerForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.label_suffix = ""
    class Meta:
        model = Hydration_Tracker
        fields = ['container_size', 'water_goal', 'active_start', 'active_end']
        widgets = {
            'container_size': forms.NumberInput(attrs={'placeholder': 'Input container size (mL) '}),
            'water_goal': forms.NumberInput(attrs={'placeholder': 'Input daily water goal (mL) '}),
            'active_start': forms.TimeInput(attrs={'placeholder': 'Input start of day (ex. 0:00) '}),
            'active_end': forms.TimeInput(attrs={'placeholder': 'Input end of day (ex. 23:59) '})
        }