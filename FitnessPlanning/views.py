from django.shortcuts import render
from django.http import HttpResponse
from .forms import (
    ExerciseRecommendationForm, CalorieDeficitPlannerForm,
    IntermittentFastingScheduleForm, FastingLogForm
)

def fitness_planning_dashboard(request):
    exercise_form = ExerciseRecommendationForm(prefix='exercise')
    deficit_form = CalorieDeficitPlannerForm(prefix='deficit')
    fasting_form = IntermittentFastingScheduleForm(prefix='fasting')
    fasting_log_form = FastingLogForm(prefix='log')

    submitted_data = {
        "exercise_result": None,
        "deficit_result": None,
        "fasting_result": None,
        "log_saved": False,
    }

    if request.method == "POST":
        if 'exercise-submit' in request.POST:
            exercise_form = ExerciseRecommendationForm(request.POST, prefix='exercise')
            if exercise_form.is_valid():
                submitted_data["exercise_result"] = exercise_form.save()
        elif 'deficit-submit' in request.POST:
            deficit_form = CalorieDeficitPlannerForm(request.POST, prefix='deficit')
            if deficit_form.is_valid():
                submitted_data["deficit_result"] = deficit_form.save()
        elif 'fasting-submit' in request.POST:
            fasting_form = IntermittentFastingScheduleForm(request.POST, prefix='fasting')
            if fasting_form.is_valid():
                submitted_data["fasting_result"] = fasting_form.save()
        elif 'log-submit' in request.POST:
            fasting_log_form = FastingLogForm(request.POST, prefix='log')
            if fasting_log_form.is_valid():
                fasting_log_form.save()
                submitted_data["log_saved"] = True

    context = {
        "exercise_form": exercise_form,
        "deficit_form": deficit_form,
        "fasting_form": fasting_form,
        "fasting_log_form": fasting_log_form,
        **submitted_data
    }
    return render(request, "fitness_planning/dashboard.html", context)
