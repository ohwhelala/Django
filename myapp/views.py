from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError

import re

def validate_password(password):
    """
    Comprehensive password validation:
    - Minimum 8 characters
    - At least one uppercase letter
    - At least one lowercase letter
    - At least one number
    - At least one special character
    """
    if len(password) < 8:
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'\d', password):
        return False
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    return True


# Registration View
def register_view(request):
    if request.method == 'POST':
        # Store these to re-populate the form
        context = {
            'username': request.POST.get('username'),
            'email': request.POST.get('email')
        }

        username = request.POST.get('username')
        password1 = request.POST.get('password')
        password2 = request.POST.get('confirm_password')
        email = request.POST.get('email')

        # First, check if passwords match
        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            context['header'] = 'Create Account'
            return render(request, 'register.html', context)

        # Add password validation BEFORE other checks
        if not validate_password(password1):
            messages.error(request, "Password must be at least 8 characters long and include uppercase, lowercase, number, and special character.")
            context['header'] = 'Create Account'
            return render(request, 'register.html', context)

        if User.objects.filter(username__iexact=username).exists():
            messages.error(request, "Username is already taken.")
            context['header'] = 'Create Account'
            return render(request, 'register.html', context)

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already in use.")
            context['header'] = 'Create Account'
            return render(request, 'register.html', context)

        try:
            user = User.objects.create_user(username=username, password=password1, email=email)
            user.save()
            messages.success(request, "Registration successful! You can now log in.")
            return redirect('login')
        except IntegrityError:
            messages.error(request, "An error occurred while creating the account. Please try again.")
            context['header'] = 'Create Account'
            return render(request, 'register.html', context)

    return render(request, 'register.html', {'header': 'Create Account'})


# Login View - Changed to use username authentication
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate with username directly
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')

    context = {'header': 'Welcome Back!'}
    return render(request, 'login.html', context)


# Logout View
def logout_view(request):
    logout(request)
    return redirect('login')


# Home View (Protected)
@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')