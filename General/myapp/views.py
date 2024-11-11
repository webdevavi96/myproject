from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login, logout as auth_logout 
from django.contrib.auth.decorators import login_required   
     # Create your views here.
     

def home(request):
    return render(request, 'index.html')
   	 
def about(request):
    return render(request, 'about.html')
   	 
def places(request):
    return render(request, 'places.html')
   	 
@login_required  	 
def booking(request):
    return render(request, 'booking.html')
    
def contactus(request):
   	return render(request, 'contactus.html')
   	 
def register(request):
    if request.method == 'POST':
        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName')
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
            user = User.objects.create_user(first_name = firstName, last_name = lastName, username=userName, email=userEmail, password=userPassword)
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
           return redirect('profile')  # Use the URL name 'index'
        else:
           return render(request, 'login.html', {'error': 'Username or password is incorrect.'})
    
    return render(request, 'login.html')
    
@login_required
def profile_page(request):
    if not request.user.is_authenticated:
       return redirect('login')  # Redirect to login page if the user is not authenticated
    
    return render(request, 'profile.html', {'user': request.user})

def logout_page(request):
    auth_logout(request)
    request.session.flush()
    return redirect('login')
    
#def new_func(request):
   # Password = request.POST.get('userPassword')
   # return Password


#for debugging perpose
def profile_page(request):
    print(f"Session ID: {request.session.session_key}", flush=True)
    if request.user.is_authenticated:
        return render(request, 'profile.html', {'user': request.user})
    return redirect('login')
