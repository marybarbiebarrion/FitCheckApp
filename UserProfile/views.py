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
            print("Form errors:", form.errors)  # Debugging: Print form errors to the console
            messages.error(request, "Please correct the errors below.")
    else:
        form = UserCreateForm()

    # Add a flag to indicate whether the form has errors
    form_has_errors = form.errors and len(form.errors) > 0

    return render(request, 'UserProfile/user_create.html', {'form': form, 'form_has_errors': form_has_errors})

def health_profile(request):
    # Logic for health profile setup
    return render(request, 'health_profile.html')

def dashboard(request):
    # Logic for dashboard
    return render(request, 'dashboard.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirect to the home page or dashboard
        else:
            messages.error(request, "Invalid username or password.")
    
    return render(request, 'UserProfile/user_login.html')

def user_logout(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('home')  # Redirect to the home page after logout