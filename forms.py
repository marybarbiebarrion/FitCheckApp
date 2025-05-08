from django import forms
from .models import BMIRecord, MoodRecord, SleepRecord

class BMIForm(forms.ModelForm):
        weight = forms.FloatField(
            label='Weight (kg)', 
            widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter weight in kilograms'})
        )
        height = forms.FloatField(
            label='Height (cm)', 
            widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter height in centimeters'})
        )

        class Meta:
            model = BMIRecord
            fields = ['user', 'weight', 'height']  
            widgets = {
                'user': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            }
class MoodForm(forms.ModelForm):
        class Meta:
            model = MoodRecord
            fields = ['user', 'mood', 'notes']
            widgets = {
                'user': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
                'mood': forms.Select(attrs={'class': 'form-control'}),
                'notes': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Any notes or comments? (Optional)', 'rows': 3}),
            }
class SleepForm(forms.ModelForm):
        class Meta:
            model = SleepRecord
            fields = ['user', 'sleep_duration', 'date', 'sleep_quality']  
            widgets = {
                'user' : forms.TextInput(attrs={
                    'class' : 'form-control',
                    'placeholder':'Enter your name'
                }),
                'sleep_duration': forms.NumberInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter sleep duration in hours',
                    'step': '0.1',
                    'min': '0'
                }),
                'date': forms.DateInput(attrs={
                    'class': 'form-control',
                    'type': 'date'
                }),
                'sleep_quality': forms.Select(attrs={
                    'class': 'form-control'
                }),
        }