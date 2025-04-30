# food_analysis/views.py
import torch
import torch.nn as nn
import torchvision.transforms as transforms
import torchvision.models as models
from torchvision.models import resnet18
from PIL import Image
import os
import csv
from django.shortcuts import render
from django.core.files.storage import default_storage
from django.conf import settings
from .models import FoodAnalysis
from .forms import FoodAnalysisForm

# Load the trained model
MODEL_PATH = os.path.join(settings.BASE_DIR, "model", "resnet18_food101.pth")
# Load the saved model data
model_data = torch.load(MODEL_PATH, map_location=torch.device("cpu"))

if isinstance(model_data, dict) and "model_state_dict" in model_data:
    print("Detected dictionary with 'model_state_dict'. Extracting weights...")

    # Initialize a new ResNet18 model
    model = models.resnet18(weights=None)
    
    # Freeze layers if needed (optional)
    for param in model.parameters():
        param.requires_grad = False

    # Modify FC layer to match the saved model
    num_ftrs = model.fc.in_features
    model.fc = nn.Sequential(
        nn.Linear(model.fc.in_features, 512),
        nn.ReLU(),
        nn.Dropout(0.5),
        nn.Linear(512, 55)  # food_classes = 55 items
    )

    # Load only the weights
    model.load_state_dict(model_data["model_state_dict"])  
    model = model.to("cpu")
    model.eval()
    print("Model loaded successfully using extracted state_dict.")

elif isinstance(model_data, dict):
    print("Detected pure state_dict. Loading into ResNet18 model...")
    model = models.resnet18(weights=None)
    
    # Adjust FC layer if needed
    num_ftrs = model.fc.in_features
    model.fc = nn.Sequential(
        nn.Linear(num_ftrs, 512),
        nn.ReLU(),
        nn.Dropout(0.5),
        nn.Linear(512, 55)  # Adjust for your number of food classes
    )
    
    model.load_state_dict(model_data, strict=False)
    model.eval()


else:
    print("Detected full model. Loading directly...")
    model = model_data
    model.eval()
    print("Model loaded successfully as a full model.")

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# Food class labels (Food-101 dataset)
food_classes = ['baby_back_ribs',
 'bibimbap',
 'caesar_salad',
 'carrot_cake',
 'cheesecake',
 'chicken_curry',
 'chicken_quesadilla',
 'chicken_wings',
 'chocolate_cake',
 'churros',
 'club_sandwich',
 'creme_brulee',
 'cup_cakes',
 'donuts',
 'dumplings',
 'french_fries',
 'french_toast',
 'fried_calamari',
 'fried_rice',
 'frozen_yogurt',
 'garlic_bread',
 'greek_salad',
 'grilled_salmon',
 'guacamole',
 'hamburger',
 'hot_dog',
 'ice_cream',
 'lasagna',
 'macaroni_and_cheese',
 'macarons',
 'mussels',
 'nachos',
 'omelette',
 'onion_rings',
 'oysters',
 'paella',
 'pancakes',
 'panna_cotta',
 'pizza',
 'pork_chop',
 'prime_rib',
 'pulled_pork_sandwich',
 'ramen',
 'red_velvet_cake',
 'sashimi',
 'scallops',
 'spaghetti_carbonara',
 'spring_rolls',
 'steak',
 'strawberry_shortcake',
 'sushi',
 'tacos',
 'takoyaki',
 'tiramisu',
 'waffles']

nutrition_file_path = os.path.join(settings.BASE_DIR, "model", "nutrition.csv")

nutrition_data = {}
with open(nutrition_file_path, mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        nutrition_data[row['label'].lower()] = {
            'calories': row['calories'],
            'protein': row['protein'],
            'carbohydrates': row['carbohydrates'],
            'fats': row['fats'],
            'fiber': row['fiber'],
            'sugars': row['sugars'],
            'sodium': row['sodium']
        }

ingredients_file_path = os.path.join(settings.BASE_DIR, "model", "ingredients.csv")

ingredients_data = {}
with open(ingredients_file_path, mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        ingredients_data[row['label'].lower()] = {
            'general_ingredients': row['general_ingredients'],
            'allergens': row['allergens']
        }


# Image preprocessing function
def preprocess_image(image_path):
    transform = transforms.Compose([
        transforms.Resize((256, 256)),  # Match training size
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406],  # Match training mean/std
                             std=[0.229, 0.224, 0.225])
    ])
    image = Image.open(image_path).convert("RGB")
    return transform(image).unsqueeze(0).to(device)


# Function to analyze image using the model
def analyze_image(image_path):
    image_tensor = preprocess_image(image_path)
    with torch.no_grad():
        outputs = model(image_tensor)
        _, predicted_idx = torch.max(outputs, 1)
        predicted_food = food_classes[predicted_idx.item()]

    # Get nutrition data from CSV based on detected food
    food_label = predicted_food.lower()
    nutrition = nutrition_data.get(food_label, {})

    # Get ingredient and allergen data
    ingredient_info = ingredients_data.get(food_label, {})
    ingredients = ingredient_info.get('general_ingredients', 'Unknown')
    allergens = ingredient_info.get('allergens', 'Unknown')
    alternatives = "Gluten-free Bread, Vegan Cheese" if "bread" in predicted_food.lower() else "None"

    # Dummy nutritional values (replace these with real data or APIs)
    # calories = 250
    # protein = 10.5
    # carbohydrates = 35.0
    # fats = 9.0
    # fiber = 2.5
    # sugars = 7.0
    # sodium = 500  # in mg

    return {
        "food_name": predicted_food,
        "ingredients": ingredients,
        "allergens": allergens,
        "alternatives": alternatives,
        "calories": nutrition.get('calories', 'N/A'),
        "protein": nutrition.get('protein', 'N/A'),
        "carbohydrates": nutrition.get('carbohydrates', 'N/A'),
        "fats": nutrition.get('fats', 'N/A'),
        "fiber": nutrition.get('fiber', 'N/A'),
        "sugars": nutrition.get('sugars', 'N/A'),
        "sodium": nutrition.get('sodium', 'N/A')
    }


def food_analysis_view(request):
    form = FoodAnalysisForm()
    analysis = None

    if request.method == 'POST':
        form = FoodAnalysisForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            image_path = default_storage.save(image.name, image)
            image_full_path = os.path.join(settings.MEDIA_ROOT, image_path)

            # Analyze image
            results = analyze_image(image_full_path)

            # Save to database
            analysis = FoodAnalysis.objects.create(
                image=image,
                food_name=results['food_name'],
                ingredients=results['ingredients'],
                allergens=results['allergens'],
                alternatives=results['alternatives'],
                calories=results['calories'],
                protein=results['protein'],
                carbohydrates=results['carbohydrates'],
                fats=results['fats'],
                fiber=results['fiber'],
                sugars=results['sugars'],
                sodium=results['sodium']
            )

    return render(request, 'food_analysis.html', {
        'form': form,
        'analysis': analysis,
        'past_analyses': FoodAnalysis.objects.all().order_by('-analyzed_at')[:5]
    })
