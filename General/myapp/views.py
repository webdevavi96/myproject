from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth.hashers import make_password

# Create your views here.
def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def places(request):
    return render(request, 'places.html')

def booking(request):
    return render(request, 'booking.html')

def contactus(request):
    return render(request, 'contactus.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        hashed_password = make_password(password)  # Hash the password

        user = User(name=name, email=email, password=hashed_password)
        user.save()  # Save user to the database
        return redirect('/login')  # Redirect to login page

    return render(request, 'register.html')
