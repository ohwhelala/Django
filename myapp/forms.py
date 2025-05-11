from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import re


# User registration form
class UserRegistrationForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'id': 'email',
            'required': True
        })
    )

    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'id': 'username',
            'required': True
        })
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'id': 'password',
            'required': True
        })
    )

    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'id': 'confirm_password',
            'required': True
        })
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username__iexact=username).exists():
            raise ValidationError("Username is already taken.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email is already in use.")
        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')

        # Password validation
        if len(password) < 8:
            raise ValidationError("Password must be at least 8 characters long.")
        if not re.search(r'[A-Z]', password):
            raise ValidationError("Password must include an uppercase letter.")
        if not re.search(r'[a-z]', password):
            raise ValidationError("Password must include a lowercase letter.")
        if not re.search(r'\d', password):
            raise ValidationError("Password must include a number.")
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            raise ValidationError("Password must include a special character.")

        return password

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise ValidationError("Passwords do not match.")

        return cleaned_data


# User login form
class UserLoginForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'id': 'username',
            'required': True
        })
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'id': 'password',
            'required': True
        })
    )


# Task form
class TaskForm(forms.ModelForm):
    due_date = forms.DateTimeField(
        required=False,
        widget=forms.DateTimeInput(attrs={
            'type': 'datetime-local',
            'id': 'due_date',
            'required': False
        })
    )

    class Meta:
        from .models import Task
        model = Task
        fields = ['title', 'description', 'due_date', 'priority', 'status']
        widgets = {
            'title': forms.TextInput(attrs={
                'id': 'title',
                'required': True
            }),
            'description': forms.Textarea(attrs={
                'id': 'description',
                'rows': 3
            }),
            'priority': forms.Select(attrs={
                'id': 'priority'
            }),
            'status': forms.Select(attrs={
                'id': 'status'
            }),
        }