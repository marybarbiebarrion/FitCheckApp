from django.db import models

class ExerciseRecommendation(models.Model):
    AEROBIC = 'Aerobic'
    ANAEROBIC = 'Anaerobic'
    EXERCISE_TYPE_CHOICES = [(AEROBIC, 'Aerobic'), (ANAEROBIC, 'Anaerobic')]

    exercise_type = models.CharField(max_length=20, choices=EXERCISE_TYPE_CHOICES)
    total_caloric_intake = models.IntegerField(default=0)
    recommended_exercise = models.TextField(default='Exercise')
    calories_burned = models.IntegerField(default=0)
    duration = models.DurationField(default="00:05:00")  # 5 minutes

class CalorieDeficitPlanner(models.Model):
    start_date = models.DateField(auto_now_add=True)
    target_date = models.DateField()
    target_weight = models.FloatField(default=0)
    daily_caloric_intake = models.IntegerField(default=0)

class IntermittentFastingSchedule(models.Model):
    FASTING_CHOICES = [('18:6', '18:6'), ('16:8', '16:8'), ('OMAD', 'One Meal A Day')]

    fasting_type = models.CharField(max_length=10, choices=FASTING_CHOICES)
    eating_window_start = models.TimeField()
    eating_window_end = models.TimeField()
    fasting_window_start = models.TimeField()
    fasting_window_end = models.TimeField()

class FastingLog(models.Model):
    date = models.DateField(auto_now_add=True)
    fasting_status = models.BooleanField(default=False)
