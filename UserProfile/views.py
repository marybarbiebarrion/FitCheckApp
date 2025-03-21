from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
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
            messages.success(request, "Account created successfully. You can now log in.")
            return redirect('user_login')  # Redirect to login page after successful registration
        else:
            messages.error(request, "Please correct the errors below.")
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
            username = form.cleaned_data.get('username')  # Retrieve username from form
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)  # Log the user in
                messages.success(request, f"Welcome back, {user.first_name}!")
                # Redirect based on whether health profile is completed
                return redirect('dashboard')  # Or 'health_profile' if needed
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'UserProfile/user_login.html', {'form': form})

def user_logout(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('home')  # Redirect to the home page after logout