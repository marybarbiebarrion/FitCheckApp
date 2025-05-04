from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import UserCreateForm

def home(request):
    return render(request, 'home.html')

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

def health_profile(request):
    return render(request, 'health_profile.html')

def dashboard(request):
    return render(request, 'dashboard.html')

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

def user_logout(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('home')
