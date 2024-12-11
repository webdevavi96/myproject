"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from myapp import views

urlpatterns = [
    path('', lambda request: redirect('home')),  # Redirect to home
    path('jet/', include('jet.urls', namespace='jet')),  # Main Jet URL
    path('jet/dashboard/', include('jet.dashboard.urls', namespace='jet-dashboard')),
    path('admin/', admin.site.urls),  # Admin interface
    path('home/', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('places/', views.places, name="places"),
    path('booking/', views.booking, name="bookings"),
    path('contactus/', views.contactus, name="contactus"),
    path('register/', views.register, name="register"),
    path('login/', views.login_page, name="login"),
    path('profile/', views.profile_page, name="profile"),
    path('logout/', views.logout_page, name="logout"),
]