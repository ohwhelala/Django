# PrioriTask: A To-Do List Application - Django Project

PrioriTask is a secure Django web application that helps users organize tasks effectively. It includes a full user authentication system (registration, login, logout, and session management) and a personalized dashboard for each user.

---

##  Features

-  User Registration & Login
-  Secure password handling (custom validation and Django's auth system)
-  User Dashboard with:
  - Profile and Account Settings
  - Task Manager with options to Add, Edit, Delete, and View tasks
  - Navigation Menu for task filtering and user options
- Task Recovery System
  - Recently deleted items accessible for 30 days
  - Automatic permanent deletion after retention period
-  Task Categorization by status and type
-  Clean and simple UI using HTML templates

---

##  Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML Templates
- **Database:** SQLite
- **Authentication:** Django's built-in auth system with custom validation

---

##  User Authentication System

###  Registration
- Route: `/register/` 
- Form includes:
  - Username (unique)
  - Email (unique)
  - Password and confirmation (custom password validator)
- Custom view manually validates and creates user

###  Login
- Accessible at `/login/`
- Validates credentials using Django’s authenticate()
- Upon success, redirects to user’s dashboard

###  Logout
- Accessible via `/logout/`
- Uses `django.contrib.auth.logout()` to end the session

###  Session Handling
- CSRF protection enabled on all forms
- Secure cookie-based session management
- User-specific content filtered by request.user

---

##  Security Features

-  Passwords are hashed using Django’s PBKDF2 hasher
-  Custom password validation: must contain uppercase, lowercase, number, and special character, and be at least 8 characters
-  CSRF tokens active on all POST forms
-  Input validation and flash messages for user feedback

---

##  Setup Instructions

```bash
# Clone the repository
git clone https://github.com/ohwhelala/Django.git
cd Django

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Start the development server
python manage.py runserver
```

##  Accessing the Django App on Mobile Devices (Local Network)

This project can be accessed on mobile devices connected to the same Wi-Fi network as your development machine. Follow these steps to make it work:

## Prerequisites

- Both your computer (running the Django server) and your mobile device must be connected to the same Wi-Fi network.
- Ensure your app is running successfully on the desktop first.
- Firewall settings may need to be adjusted (see below).
