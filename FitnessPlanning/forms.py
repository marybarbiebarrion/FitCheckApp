from django import forms
from .models import ExerciseRecommendation, CalorieDeficitPlanner, IntermittentFastingSchedule, FastingLog

class ExerciseRecommendationForm(forms.ModelForm):
    class Meta:
        model = ExerciseRecommendation
        fields = ['exercise_type', 'total_caloric_intake', 'recommended_exercise', 'calories_burned', 'duration']

class CalorieDeficitPlannerForm(forms.ModelForm):
    class Meta:
        model = CalorieDeficitPlanner
        fields = ['target_date', 'target_weight', 'daily_caloric_intake']

class IntermittentFastingScheduleForm(forms.ModelForm):
    class Meta:
        model = IntermittentFastingSchedule
        fields = ['fasting_type', 'eating_window_start', 'eating_window_end', 'fasting_window_start', 'fasting_window_end']

class FastingLogForm(forms.ModelForm):
    class Meta:
        model = FastingLog
        fields = ['fasting_status']
