from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserCreateForm
from django.contrib import messages

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
    return render(request, 'UserProfile/user_create.html', {'form': form})

def health_profile(request):
    # Logic for health profile setup
    return render(request, 'health_profile.html')

def dashboard(request):
    # Logic for dashboard
    return render(request, 'dashboard.html')

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')  # Username or email
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                user_login(request, user)
                # Redirect based on whether health profile is completed
                return redirect('dashboard')  # Or 'health_profile' if needed
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'UserProfile/user_login.html', {'form': form})
