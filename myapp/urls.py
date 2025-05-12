from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    # Root URL should check authentication
    path('', views.landing_view, name='landing'),

    # Authentication URLs
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Task URLs
    path('home/', login_required(views.home), name='home'),
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/<int:pk>/', views.task_detail, name='task_detail'),
    path('tasks/new/', views.task_create, name='task_create'),
    path('tasks/<int:pk>/edit/', views.task_update, name='task_update'),
    path('tasks/<int:pk>/delete/', views.task_delete, name='task_delete'),
    path('tasks/<int:pk>/complete/', views.task_complete, name='task_complete'),
]
