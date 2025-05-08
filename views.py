from django.shortcuts import render
from .models import BMIRecord, MoodRecord, SleepRecord
from .forms import BMIForm, MoodForm, SleepForm
from wellnesstracker import models
from django.shortcuts import redirect

def bmi_form(request):
    result = None
    category = None
    form = BMIForm(request.POST or None)
    if form.is_valid():
        bmi_record = form.save(commit=False)
        bmi = bmi_record.calculate_bmi(
            form.cleaned_data['weight'], form.cleaned_data['height']
        )
        category = bmi_record.get_bmi_category(bmi)
        bmi_record.initial_bmi = bmi
        bmi_record.current_bmi = bmi
        bmi_record.category = category
        bmi_record.save() 
        result = bmi
        category = category

    return render(request, 'bmi_form.html', 
                  {'form': form,
                   'result': result,
                   'category': category,
                   })
def mood_form(request):
    form = MoodForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('wellnesstracker:mood_form') 
    return render(request, 'mood_form.html', {'form': form})
def sleep_form(request):
    form = SleepForm(request.POST or None)
    sleep_records = SleepRecord.objects.order_by('-created_on')

    if form.is_valid():
        form.save()
        return redirect('wellnesstracker:sleep_form')

    return render(request, 'sleep_form.html', {
        'form': form,
        'sleep_records': sleep_records
    })
def past_analyses(request):
    bmi_records = BMIRecord.objects.all().order_by('-created_on')
    mood_records = MoodRecord.objects.all().order_by('-created_on')
    sleep_records = SleepRecord.objects.all().order_by('-date')

    context = {
        'bmi_records': bmi_records,
        'mood_records': mood_records,
        'sleep_records': sleep_records,
    }
    return render(request, 'past_analyses.html', context)

