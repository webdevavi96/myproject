from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login	 
#from django.contrib.auth.decorators import login_required   	
     # Create your views here.
#@login_required(login_url='login')	 

def home(request):
    return render(request, 'index.html')
   	 
def about(request):
    return render(request, 'about.html')
   	 
def places(request):
    return render(request, 'places.html')
   	 
   	 
def booking(request):
    return render(request, 'booking.html')
    
def contactus(request):
   	return render(request, 'contactus.html')
   	 
def register(request):
    if request.method == 'POST':
        userName = request.POST.get('userName')
        userEmail = request.POST.get('userEmail')
        userPassword = request.POST.get('userPassword')
        confirmPassword = request.POST.get('confirmPassword')
        
        if userPassword != confirmPassword:
            return HttpResponse("Password did not match. Please enter a valid password.")
        
        # Check if the username already exists
        if User.objects.filter(username=userName).exists():
           return HttpResponse("Username is already taken. Please choose another one.")
                                    
        else:
            # Create a new user
            user = User.objects.create_user(username=userName, email=userEmail, password=userPassword)
            user.save()
            return redirect('login')  # Use the URL name 'login'
    
    return render(request, 'register.html')

def login_page(request):
    if request.method == 'POST':
        userName = request.POST.get('userName')
        Password = request.POST.get('userPassword')
        # Authenticate user
        user = authenticate(request, username=userName, password=Password)
        
        if user is not None:
           auth_login(request, user)
           return redirect('home')  # Use the URL name 'index'
        else:
           return HttpResponse("Username or password is incorrect. Please check your credentials.")
    
    return render(request, 'login.html')

def new_func(request):
    Password = request.POST.get('userPassword')
    return Password

