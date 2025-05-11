from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.db import IntegrityError
from .forms import TaskForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Task


# Import your forms
from .forms import UserRegistrationForm, UserLoginForm, TaskForm

# Registration View
def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            try:
                user = User.objects.create_user(username=username, password=password, email=email)
                user.save()
                messages.success(request, "Registration successful! You can now log in.")
                return redirect('login')
            except IntegrityError:
                messages.error(request, "An error occurred while creating the account. Please try again.")
    else:
        form = UserRegistrationForm()

    return render(request, 'register.html', {'form': form})


# Login View
def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password.")
                return redirect('login')
    else:
        form = UserLoginForm()

    return render(request, 'login.html', {'form': form})


# Logout View (remains the same)
def logout_view(request):
    logout(request)
    return redirect('login')


# Home View (remains the same)
@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')


# Task list view (Read operation)
@login_required(login_url='login')
def task_list(request):
    # Get all tasks for the current user
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'home.html', {'tasks': tasks})


# Task detail view (Read operation for a single task)
@login_required(login_url='login')
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    return render(request, 'task_detail.html', {'task': task})


# Task create view (Create operation)
@login_required(login_url='login')
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            messages.success(request, "Task created successfully!")
            return redirect('home')  # Ensure this redirects to home, not task_list
    else:
        form = TaskForm()

    return render(request, 'task_form.html', {'form': form, 'title': 'Create Task'})


# Task update view (Update operation)
@login_required(login_url='login')
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, "Task updated successfully!")
            return redirect('home')
    else:
        form = TaskForm(instance=task)

    return render(request, 'task_form.html', {'form': form, 'title': 'Update Task'})


# Task delete view (Delete operation)
@login_required(login_url='login')
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)

    if request.method == 'POST':
        task.delete()
        messages.success(request, "Task deleted successfully!")
        return redirect('task_list')

    return render(request, 'task_confirm_delete.html', {'task': task})


@login_required
def task_detail(request, pk):
    """
    View function for displaying a single task's details.
    """
    # Only fetch tasks that belong to the current logged-in user
    task = get_object_or_404(Task, pk=pk, user=request.user)

    return render(request, 'task_detail.html', {'task': task})

def landing_view(request):
    """
    Landing view that redirects to home if authenticated,
    otherwise redirects to login page
    """
    if request.user.is_authenticated:
        return redirect('home')
    else:
        return redirect('login')