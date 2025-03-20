# food_analysis/views.py
import torch
from django.shortcuts import render
from django.core.files.storage import default_storage
from .models import FoodAnalysis
from .forms import FoodAnalysisForm
import os
from django.conf import settings

## Load Required Libraries
import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision
import torchvision.transforms as transforms
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import ipywidgets as widgets
import torchvision.models as models

# Load the trained ResNet model
MODEL_PATH = os.path.join(settings.BASE_DIR, "model", "food101_model.pth")

# Food Classification and Nutrition Analysis
# Load the saved model data
model_data = torch.load(MODEL_PATH, map_location=torch.device("cpu"))

if isinstance(model_data, dict) and "model_state_dict" in model_data:
    print("Detected dictionary with 'model_state_dict'. Extracting weights...")

    # Initialize a new ResNet50 model
    model = models.resnet50(pretrained=False)

    # Modify FC layer to match the saved model
    num_ftrs = model.fc.in_features
    model.fc = nn.Sequential(
        nn.Linear(num_ftrs, 512),  # Adjust this to match your saved model
        nn.ReLU(),
        nn.Linear(512, 101)  # Assuming Food101 has 101 classes
    )

    # Load only the weights
    model.load_state_dict(model_data["model_state_dict"], strict=False)  # Allow mismatches
    model.eval()
    print("Model loaded successfully using extracted state_dict.")

elif isinstance(model_data, dict):
    print("Detected pure state_dict. Loading into ResNet50 model...")
    model = models.resnet50(pretrained=False)
    model.load_state_dict(model_data, strict=False)  # Allow mismatches
    model.eval()
    print("Model loaded successfully using state_dict.")

else:
    print("Detected full model. Loading directly...")
    model = model_data
    model.eval()
    print("Model loaded successfully as a full model.")

def analyze_image(image_path):
    # Implement image analysis using ResNet model
    # This is a placeholder for actual image preprocessing & inference
    return {
        "ingredients": "Tomato, Cheese, Dough",
        "allergens": "Dairy, Gluten",
        "alternatives": "Gluten-free Dough, Vegan Cheese"
    }

def food_analysis_view(request):
    if request.method == 'POST':
        form = FoodAnalysisForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            image_path = default_storage.save(image.name, image)
            results = analyze_image(image_path)
            
            analysis = FoodAnalysis.objects.create(
                image=image,
                ingredients=results['ingredients'],
                allergens=results['allergens'],
                alternatives=results['alternatives']
            )
            
            return render(request, 'food_analysis.html', {
                'form': form,
                'analysis': analysis,
                'past_analyses': FoodAnalysis.objects.all().order_by('-analyzed_at')[:5]
            })
    else:
        form = FoodAnalysisForm()

    return render(request, 'food_analysis.html', {'form': form, 'past_analyses': FoodAnalysis.objects.all().order_by('-analyzed_at')[:5]})
