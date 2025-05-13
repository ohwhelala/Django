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
---

##  Accessing the Django App on Mobile Devices (Local Network)

This project can be accessed on mobile devices connected to the same Wi-Fi network as your development machine. Follow these steps to make it work:

## Prerequisites

- Both your computer (running the Django server) and your mobile device must be connected to the same Wi-Fi network.
- Ensure your app is running successfully on the desktop first.
- Firewall settings may need to be adjusted (see below).

## Steps to Enable Mobile Access

### 1. Run the Django Server on All Interfaces
By default, Django runs on 127.0.0.1, which is only accessible from your computer. Run the server on 0.0.0.0 instead:

```bash
python manage.py runserver 0.0.0.0:8000
```
This tells Django to listen for requests from any device on the network.

### 2. Find Your Local IP Address
On your development machine (Windows example):
- Open Command Prompt and run:
```bash
ipconfig
```

- Look for the IPv4 Address, e.g.:
```bash
IPv4 Address. . . . . . . . . . . : 192.168.1.22
```

This is the IP address your mobile device will use to access the server.

### 3. Add Local IP to ALLOWED_HOSTS
In your Django project’s settings.py, update the ALLOWED_HOSTS setting to include your local IP address:

```bash
ALLOWED_HOSTS = ['192.168.1.22', 'localhost', '127.0.0.1']
```
Replace 192.168.1.22 with your actual local IP address.

### 4. Access the App from Mobile Browser
On your mobile device, open a browser and navigate to:
```bash
http://192.168.1.22:8000
```
(Again, replace with your actual IP address.)

### 5. Optional: Adjust Firewall Settings
If your mobile device cannot connect:
- Allow Python through your computer’s firewall (especially on Windows).
- Temporarily disable firewall to test (not recommended long-term).
- Ensure port 8000 is not blocked by security software.
