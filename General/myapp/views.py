from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout 	 
#from django.contrib.auth.decorators import login_required   	
     # Create your views here.
#@login_required(login_url='login')	 
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
   	 
def register(request):
    if request.method == 'POST':
        userName = request.POST.get('userName')
        userEmail = request.POST.get('userEmail')
        userPassword = request.POST.get('userPassword')
        confirmPassword = request.POST.get('confirmPassword')
        
        if userPassword != confirmPassword:
            return HttpResponse("Password did not match. Please enter a valid password.")
        else:
            # Create a new user
            user = User.objects.create_user(username=userName, email=userEmail, password=userPassword)
            user.save()
            return redirect('login.html')  # Use the URL name 'login'
    
    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        userName = request.POST.get('userName')
        userPassword = request.POST.get('userPassword')
        
        # Authenticate user
        user = authenticate(request, username=userName, password=userPassword)
        
        if user is not None:
            login(request, user)
            return redirect('home')  # Use the URL name 'home'
        else:
            return HttpResponse("Username or password is incorrect. Please check your credentials.")
    
    return render(request, 'login.html')

