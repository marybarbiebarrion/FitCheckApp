from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import UserCreateForm

def home(request):
    return render(request, 'home.html')  # Render a home page template

def user_create(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = UserCreateForm()
    return render(request, 'UserCreate/user_create.html', {'form': form})

def health_profile(request):
    # Logic for health profile setup
    return render(request, 'health_profile.html')

def dashboard(request):
    # Logic for dashboard
    return render(request, 'dashboard.html')
