from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import UserCreateForm, EditProfileForm, HealthProfileForm  # Import your new health profile form
from .models import User  # Make sure your User model is correctly imported
from django.http import HttpResponse

# User Creation view (no change)
def user_create(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Account created successfully. You can now log in.")
            return redirect('user_login')
        else:
            print("Form errors:", form.errors)
            messages.error(request, "Please correct the errors below.")
    else:
        form = UserCreateForm()

    form_has_errors = form.errors and len(form.errors) > 0

    return render(request, 'UserProfile/user_create.html', {'form': form, 'form_has_errors': form_has_errors})

# views.py
def health_profile(request):
    user = request.user

    if request.method == 'POST':
        form = HealthProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Your health profile has been updated!")
            return redirect('dashboard')
    else:
        form = HealthProfileForm(instance=user)

    return render(request, 'UserProfile/health_profile.html', {
        'form': form,
        'user_health_profile': user
    })

# User Login View (no change)
def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid email or password.")

    return render(request, 'UserProfile/user_login.html')

# Logout View (no change)
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('UserProfile/user_login.html')  # or wherever you want the user to go after logout
    return render(request, 'UserProfile/user_logout.html')  # shows confirmation page

# Splash Page View (no change)
def splash(request):
    return render(request, 'splash.html')

# Dashboard View (updated to include the nickname from user)
def dashboard_view(request):
    context = {
        'nickname': request.user.nickname if request.user.is_authenticated else 'Guest'
    }
    return render(request, 'dashboard.html', context)

# Edit Profile View (no change)
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # After saving, redirect to a profile page or dashboard
    else:
        form = EditProfileForm(instance=request.user)
    
    return render(request, 'UserProfile/edit_profile.html', {'form': form})

# views.py

import random
from django.shortcuts import render

def get_fitness_trivia():
    # Expanded list of fitness trivia (static content)
    trivia = [
        "Did you know? Walking 30 minutes a day can help reduce the risk of heart disease.",
        "Regular exercise can increase your lifespan by up to 5 years.",
        "Drinking water before meals can help you reduce calorie intake and manage weight.",
        "Strength training can help improve bone density and prevent osteoporosis.",
        "Exercising outdoors can boost your mood and reduce stress levels.",
        "High-intensity interval training (HIIT) can help burn fat and improve metabolism.",
        "Stretching before and after exercise can help prevent injuries and improve flexibility.",
        "A balanced diet, combined with regular exercise, is the key to maintaining a healthy weight.",
        "Yoga is not only for flexibility but can also improve mental clarity and reduce stress.",
        "Getting enough sleep is essential for recovery and improving athletic performance.",
        "Drinking green tea can help boost your metabolism and assist in fat burning.",
        "Lifting weights can help increase your muscle mass and improve your metabolism.",
        "A healthy diet rich in fruits, vegetables, and whole grains can reduce inflammation in the body.",
        "Running regularly can help reduce your risk of chronic diseases such as diabetes, heart disease, and high blood pressure.",
        "Protein is an important nutrient for muscle repair, especially after an intense workout.",
        "Exercising with a friend or in a group can increase motivation and make it more fun.",
        "Cycling can improve cardiovascular health, increase stamina, and is easy on the joints.",
        "Maintaining a consistent exercise routine is more beneficial than working out sporadically.",
        "Stretching can help increase circulation and improve flexibility, which aids in better movement.",
        "Eating smaller, balanced meals throughout the day can help maintain energy levels and reduce overeating.",
        "Cardio exercises like swimming, jogging, or cycling can help improve lung capacity and heart health.",
        "Drinking water is essential for proper muscle function and preventing cramps during exercise.",
        "Exercising can help improve your posture by strengthening the muscles that support your spine.",
        "Incorporating strength training into your fitness routine can help prevent muscle loss as you age.",
        "A good pre-workout meal should be high in carbohydrates and moderate in protein to provide energy during exercise.",
        "Mental health benefits of exercise include reduced anxiety, depression, and better sleep quality.",
        "Avoiding sugary drinks and opting for water or natural juices can improve overall health and weight management.",
        "To maintain balance, aim to include both cardio and strength training exercises in your workout routine.",
        "Research shows that exercising in nature can improve both physical and mental health.",
        "Dancing is a great way to exercise, improve coordination, and boost your mood.",
        "When it comes to weight loss, focusing on overall lifestyle changes, including diet and exercise, is more effective than just cutting calories.",
        "Exercising in the morning may boost your metabolism for the rest of the day.",
        "An exercise routine that includes a variety of activities, such as cardio, strength, and flexibility training, helps keep things interesting and challenging.",
        "A healthy body relies on a balance of good nutrition, physical activity, and mental well-being.",
        "The brain benefits from exercise by improving memory, focus, and overall cognitive function.",
        "Drinking enough water before, during, and after exercise can prevent dehydration and improve workout performance.",
        "Spending time outdoors in the sun (with proper sunscreen) can boost vitamin D levels and promote bone health.",
        "Physical activity increases blood flow to the brain and can improve mood by releasing endorphins.",
        "Even small amounts of exercise can lead to significant health benefits, such as improved cardiovascular health and better mental health.",
        "Exercise can help prevent age-related cognitive decline and keep your brain sharp as you age.",
        "Muscle recovery time varies based on the intensity of the workout and the individual’s fitness level.",
        "Incorporating rest days into your workout routine is important for muscle repair and overall well-being.",
        "Regular physical activity can improve sleep quality, reduce the time it takes to fall asleep, and increase deep sleep.",
        "Healthy fats found in avocados, nuts, and olive oil can support brain health and energy levels."
    ]
    
    # Pick a random trivia fact
    return random.choice(trivia)

def dashboard(request):
    # Get a random fitness trivia
    fitness_trivia = get_fitness_trivia()
    return render(request, 'dashboard.html', {'fitness_trivia': fitness_trivia})
