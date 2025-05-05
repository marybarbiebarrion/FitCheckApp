from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import UserCreateForm, EditProfileForm, HealthProfileForm


def user_create(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Account created successfully. You can now log in.")
            return redirect('UserProfile:user_login')
        else:
            print("Form errors:", form.errors)
            messages.error(request, "Please correct the errors below.")
    else:
        form = UserCreateForm()

    form_has_errors = form.errors and len(form.errors) > 0

    return render(request, 'UserProfile/user_create.html', {'form': form, 'form_has_errors': form_has_errors})

def health_profile(request):
    user = request.user  # Get the currently logged-in user
    if request.method == 'POST':
        # If it's a POST request, it means the user is submitting a form
        form = HealthProfileForm(request.POST, instance=user)  # Bind the form to the user
        if form.is_valid():
            form.save()  # Save the form if it's valid
            messages.success(request, "Your health profile has been updated!")
            return redirect('UserProfile/health_profile')  # Redirect to the same page
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        # If it's a GET request, show the health profile form populated with the user's data
        form = HealthProfileForm(instance=user)  # Populate form with existing health data

    return render(request, 'UserProfile/health_profile.html', {'form': form})

def dashboard(request):
    return render(request, 'dashboard.html')

def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('UserProfile:dashboard')
        else:
            messages.error(request, "Invalid email or password.")

    return render(request, 'UserProfile/user_login.html')

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('UserProfile/user_login.html')  # or wherever you want the user to go after logout
    return render(request, 'UserProfile/user_logout.html')  # shows confirmation page

def splash(request):
    return render(request, 'splash.html')

def dashboard_view(request):
    context = {
        'nickname': request.user.nickname if request.user.is_authenticated else 'Guest'
    }
    return render(request, 'dashboard.html', context)

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('UserProfile:dashboard')  # After saving, redirect to a profile page or dashboard
    else:
        form = EditProfileForm(instance=request.user)
    
    return render(request, 'UserProfile/edit_profile.html', {'form': form})