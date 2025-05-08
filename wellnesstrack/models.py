from django.db import models
from django.utils.timezone import now
from django.utils import timezone


class BMIRecord(models.Model):
    user = models.CharField(max_length=50)
    initial_bmi = models.FloatField(default=0)
    current_bmi = models.FloatField()
    CATEGORY_CHOICES = [
        ('Underweight', 'Underweight'),
        ('Normal', 'Normal'),
        ('Overweight', 'Overweight'),
        ('Obese', 'Obese'),
    ]
    category = models.CharField(max_length=20,
                                choices=CATEGORY_CHOICES,
                                default='Normal')
    created_on = models.DateTimeField(default=now)

    def calculate_bmi(self, weight, height):
        height_m = height / 100
        bmi = weight / (height_m**2)
        return round(bmi, 2)

    def get_bmi_category(self, bmi):
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 24.9:
            return "Normal"
        elif 25 <= bmi < 29.9:
            return "Overweight"
        else:
            return "Obese"

    def __str__(self):
        return f"{self.user} - Current BMI: {self.current_bmi:.2f} ({self.category})"

class MoodRecord(models.Model):
    MOOD_CHOICES = [
        ('Happy', 'Happy 😊'),
        ('Normal', 'Normal 😐'),
        ('Sad', 'Sad 😢'),
        ('Awful', 'Awful 😡'),
    ]
    user = models.CharField(max_length = 100)
    mood = models.CharField(max_length=10,
                            choices=MOOD_CHOICES,
                            default='Normal')
    notes = models.TextField(blank=True, null=True)
    created_on = models.DateField(default=now)

    def __str__(self):
        return f"{self.user} - Mood: {self.mood}"
class SleepRecord(models.Model):
    user = models.CharField(max_length=100)
    sleep_duration = models.FloatField()
    sleep_quality = models.CharField(  
        max_length=50,
        choices=[
            ('Excellent', 'Excellent 🌟'),
            ('Good', 'Good 🙂'),
            ('Fair', 'Fair 😐'),
            ('Poor', 'Poor 😴')
        ],
        default='Good'
    )
    created_on = models.DateTimeField(auto_now_add=True)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.user} - {self.sleep_duration} hrs - Quality: {self.sleep_quality} on {self.date}"


