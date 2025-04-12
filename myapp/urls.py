from django.urls import path
from . import views

urlpatterns = [
    # Change home_view to home to match the function name in views.py
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
]