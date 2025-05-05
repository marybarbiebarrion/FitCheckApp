from django import forms
from datetime import timedelta
from .models import (
    ExerciseRecommendation,
    CalorieDeficitPlanner,
    IntermittentFastingSchedule,
    FastingLog
)
from .fitness_utils import (
    calculate_exercise_recommendation,
    calculate_if_schedule
)

class ExerciseRecommendationForm(forms.ModelForm):
    class Meta:
        model = ExerciseRecommendation
        fields = ['exercise_type', 'total_caloric_intake']

    def save(self, commit=True):
        instance = super().save(commit=False)

        result = calculate_exercise_recommendation(
            self.cleaned_data['total_caloric_intake'],
            self.cleaned_data['exercise_type']
        )

        instance.recommended_exercise = result['recommended_exercise']
        instance.calories_burned = result['calories_burned']
        instance.duration = timedelta(minutes=result['duration_minutes'])

        if commit:
            instance.save()
        return instance


class CalorieDeficitPlannerForm(forms.ModelForm):
    class Meta:
        model = CalorieDeficitPlanner
        fields = ['current_weight', 'target_weight', 'target_date']

    # Making the target_date a DateField (this will render as a date input in the form)
    target_date = forms.DateField(widget=forms.SelectDateWidget(), required=True)

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        return instance


class IntermittentFastingScheduleForm(forms.ModelForm):
    class Meta:
        model = IntermittentFastingSchedule
        fields = ['fasting_type', 'eating_window_start']

    # Making fields optional by setting required=False
    fasting_type = forms.ChoiceField(choices=IntermittentFastingSchedule.FASTING_CHOICES, required=False)
    eating_window_start = forms.TimeField(required=False)

    def save(self, commit=True):
        instance = super().save(commit=False)

        # Calculate fasting and eating windows only if the fields are filled out
        if self.cleaned_data.get('fasting_type') and self.cleaned_data.get('eating_window_start'):
            result = calculate_if_schedule(
                self.cleaned_data['fasting_type'],
                self.cleaned_data['eating_window_start']
            )

            instance.eating_window_end = result['eating_window_end']
            instance.fasting_window_start = result['fasting_window_start']
            instance.fasting_window_end = result['fasting_window_end']

        if commit:
            instance.save()
        return instance


class FastingLogForm(forms.ModelForm):
    class Meta:
        model = FastingLog
        fields = ['fasting_status']
