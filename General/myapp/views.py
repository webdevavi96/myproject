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
           return HttpResponse("Password did not macth. Please enter a valid Password.")
        else:
            newUser = User.objects.create_user(username=userName,useremail=userEmail,Password=userPassword)
            newUser.save()
            return redirect('login.html')
    return render(request, 'register.html')
def login(request):
    if request.method == 'POST':
       userName = request.POST.get('userName')
       userPassword = request.POST.get('userPassword')
       user = authenticate(request, userName = userName, userPassword = userPassword)
       if user is not None:
           login(request, user)
           return redirect('home')
       else:
           return HttpResponse("username or password is Incorrect. Please check and enter again to Login into your account.")
    return render(request, 'login.html')