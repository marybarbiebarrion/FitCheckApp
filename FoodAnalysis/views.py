# food_analysis/views.py
import torch
import torch.nn as nn
import torchvision.transforms as transforms
import torchvision.models as models
from PIL import Image
import os
from django.shortcuts import render
from django.core.files.storage import default_storage
from django.conf import settings
from .models import FoodAnalysis
from .forms import FoodAnalysisForm

# Load the trained model
MODEL_PATH = os.path.join(settings.BASE_DIR, "model", "food101_model.pth")
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

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# Food class labels (Food-101 dataset)
food_classes = [
    'apple_pie', 'baby_back_ribs', 'baklava', 'beef_carpaccio', 'beef_tartare',
    'beet_salad', 'beignets', 'bibimbap', 'bread_pudding', 'breakfast_burrito',
    'bruschetta', 'caesar_salad', 'cannoli', 'caprese_salad', 'carrot_cake',
    'ceviche', 'cheesecake', 'cheese_plate', 'chicken_curry', 'chicken_quesadilla',
    'chicken_wings', 'chocolate_cake', 'chocolate_mousse', 'churros', 'clam_chowder',
    'club_sandwich', 'crab_cakes', 'creme_brulee', 'croque_madame', 'cup_cakes',
    'deviled_eggs', 'donuts', 'dumplings', 'edamame', 'eggs_benedict',
    'escargots', 'falafel', 'filet_mignon', 'fish_and_chips', 'foie_gras',
    'french_fries', 'french_onion_soup', 'french_toast', 'fried_calamari', 'fried_rice',
    'frozen_yogurt', 'garlic_bread', 'gnocchi', 'greek_salad', 'grilled_cheese_sandwich',
    'grilled_salmon', 'guacamole', 'gyoza', 'hamburger', 'hot_and_sour_soup',
    'hot_dog', 'huevos_rancheros', 'hummus', 'ice_cream', 'lasagna',
    'lobster_bisque', 'lobster_roll_sandwich', 'macaroni_and_cheese', 'macarons', 'miso_soup',
    'mussels', 'nachos', 'omelette', 'onion_rings', 'oysters',
    'pad_thai', 'paella', 'pancakes', 'panna_cotta', 'peking_duck',
    'pho', 'pizza', 'pork_chop', 'poutine', 'prime_rib',
    'pulled_pork_sandwich', 'ramen', 'ravioli', 'red_velvet_cake', 'risotto',
    'samosa', 'sashimi', 'scallops', 'seaweed_salad', 'shrimp_and_grits',
    'spaghetti_bolognese', 'spaghetti_carbonara', 'spring_rolls', 'steak', 'strawberry_shortcake',
    'sushi', 'tacos', 'takoyaki', 'tiramisu', 'tuna_tartare', 'waffles'
]

# Image preprocessing function
def preprocess_image(image_path):
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    image = Image.open(image_path).convert("RGB")
    return transform(image).unsqueeze(0)

# Function to analyze image using the model
def analyze_image(image_path):
    image_tensor = preprocess_image(image_path)
    with torch.no_grad():
        outputs = model(image_tensor)
        _, predicted_idx = torch.max(outputs, 1)
        predicted_food = food_classes[predicted_idx.item()]

    # Dummy data for allergens & alternatives (You can replace with real data)
    allergens = "Dairy, Gluten" if "cheese" in predicted_food.lower() else "None"
    alternatives = "Gluten-free Bread, Vegan Cheese" if "bread" in predicted_food.lower() else "None"

    return {
        "food_name": predicted_food,
        "ingredients": "Tomato, Cheese, Dough",
        "allergens": allergens,
        "alternatives": alternatives
    }

# Django view for food analysis
def food_analysis_view(request):
    if request.method == 'POST':
        form = FoodAnalysisForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            image_path = default_storage.save(image.name, image)
            image_full_path = os.path.join(settings.MEDIA_ROOT, image_path)

            # Run model prediction
            results = analyze_image(image_full_path)

            # Save results in database
            analysis = FoodAnalysis.objects.create(
                image=image,
                food_name=results['food_name'],
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
