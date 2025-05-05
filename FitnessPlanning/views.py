from django.shortcuts import render
from django.utils import timezone
from datetime import datetime, timedelta
from .forms import (
    ExerciseRecommendationForm,
    CalorieDeficitPlannerForm,
    IntermittentFastingScheduleForm,
    FastingLogForm
)
from .fitness_utils import calculate_if_schedule
from .models import (
    ExerciseRecommendation,
    CalorieDeficitPlanner,
    IntermittentFastingSchedule,
    FastingLog
)

def fitness_planning_dashboard(request):
    # Initialize forms for each section
    exercise_form = ExerciseRecommendationForm(request.POST or None)
    deficit_form = CalorieDeficitPlannerForm(request.POST or None)
    fasting_form = IntermittentFastingScheduleForm(request.POST or None)
    fasting_log_form = FastingLogForm(request.POST or None)

    # Initialize variables to store results
    exercise_result = deficit_result = fasting_result = None
    log_saved = False
    window_status = ''
    schedule = {}

    eating_window_start = eating_window_end = fasting_window_start = fasting_window_end = None

    current_time = timezone.now()  

    if request.method == 'POST':
        if 'exercise-submit' in request.POST and exercise_form.is_valid():
            exercise_result = exercise_form.save()

        elif 'deficit-submit' in request.POST and deficit_form.is_valid():
            deficit_result = deficit_form.save()

        elif 'fasting-submit' in request.POST and fasting_form.is_valid():
            fasting_result = fasting_form.save()

            fasting_type = fasting_form.cleaned_data.get('fasting_type')
            eating_start_time = fasting_form.cleaned_data.get('eating_window_start')

            if fasting_type and eating_start_time:

                schedule = calculate_if_schedule(fasting_type, eating_start_time)

                if schedule and 'eating_window_start' in schedule and 'eating_window_end' in schedule:
                    eating_window_start = schedule.get('eating_window_start')
                    eating_window_end = schedule.get('eating_window_end')
                    fasting_window_start = schedule.get('fasting_window_start')
                    fasting_window_end = schedule.get('fasting_window_end')

                    eating_window_start = timezone.make_aware(datetime.combine(datetime.today(), eating_window_start))
                    eating_window_end = timezone.make_aware(datetime.combine(datetime.today(), eating_window_end))
                    current_time_aware = timezone.make_aware(datetime.combine(datetime.today(), current_time.time()))

                    if eating_window_start <= current_time_aware <= eating_window_end:
                        window_status = "You are in your eating window."
                    else:
                        window_status = "You are in your fasting window."

        elif 'log-submit' in request.POST and fasting_log_form.is_valid():
            fasting_log_form.save()
            log_saved = True


    context = {
        'exercise_form': exercise_form,
        'deficit_form': deficit_form,
        'fasting_form': fasting_form,
        'fasting_log_form': fasting_log_form,
        'exercise_result': exercise_result,
        'deficit_result': deficit_result,
        'fasting_result': fasting_result,
        'log_saved': log_saved,
        'window_status': window_status,
        'schedule': schedule,
        'eating_window_start': eating_window_start,
        'eating_window_end': eating_window_end,
        'fasting_window_start': fasting_window_start,
        'fasting_window_end': fasting_window_end,
        'current_time': current_time, 
        'exercise_entries': ExerciseRecommendation.objects.all().order_by('-id')[:5],
        'deficit_entries': CalorieDeficitPlanner.objects.all().order_by('-start_date')[:5],
        'fasting_schedules': IntermittentFastingSchedule.objects.all().order_by('-id')[:5],
        'fasting_logs': FastingLog.objects.all().order_by('-date')[:5],
    }

    return render(request, 'dashboard.html', context)
