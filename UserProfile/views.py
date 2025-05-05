from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import UserCreateForm, EditProfileForm


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