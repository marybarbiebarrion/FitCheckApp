from django import forms
from .models import FoodAnalysis

class FoodAnalysisForm(forms.ModelForm):
    class Meta:
        model = FoodAnalysis
        fields = ['image']