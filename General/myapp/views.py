from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login, logout as auth_logout 
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required   
#import logging

     # Create your views here.
     
#logger = logging.getLogger(__name__)


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
   	 
"""
def register(request):
    if request.method == 'POST':
        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName')
        userName = request.POST.get('userName')
        userEmail = request.POST.get('userEmail')
        userPhone = request.POST.get('userPhone')
        userPassword = request.POST.get('userPassword')
        confirmPassword = request.POST.get('confirmPassword')
        
        if userPassword != confirmPassword:
            return HttpResponse("Password did not match. Please enter a valid password.")
        
        # Check if the username already exists
        if User.objects.filter(username=userName).exists():
           return HttpResponse("Username is already taken. Please choose another one.")
                                    
        else:
            # Create a new user
            user = User.objects.create_user(first_name = firstName, last_name = lastName, username=userName, email=userEmail,password = userPassword, phone_number = userPhone)
            user.save()
            return redirect('login')  # Use the URL name 'login'
    
    return render(request, 'register.html')
    
"""

def register(request):
    if request.method == 'POST':
        firstName = request.POST.get('firstName', '').strip()
        lastName = request.POST.get('lastName', '').strip()
        userName = request.POST.get('userName', '').strip()
        userEmail = request.POST.get('userEmail', '').strip()
        userPhone = request.POST.get('userPhone', '').strip()
        userPassword = request.POST.get('userPassword', '').strip()
        confirmPassword = request.POST.get('confirmPassword', '').strip()
        
        # Check for empty fields
        if not all([firstName, lastName, userName, userEmail, userPhone, userPassword, confirmPassword]):
            return HttpResponse("All fields are required. Please fill out the form completely.")
        
        # Password mismatch check
        if userPassword != confirmPassword:
            return HttpResponse("Passwords do not match. Please try again.")
        
        # Check if the username already exists
        if User.objects.filter(username=userName).exists():
            return HttpResponse("Username is already taken. Please choose another one.")
        
        # Check if email is already registered
        if User.objects.filter(email=userEmail).exists():
            return HttpResponse("Email is already registered. Please use a different email address.")
        
        # Create a new user
        user = User.objects.create_user(
          first_name=firstName,
          last_name=lastName,
          username=userName,
          email=userEmail,
          password=userPassword  # Password will be hashed
        )
        user.save()
        
        # Redirect to login page
      return redirect('login')  # Make sure 'login' is defined in your URL patterns
    
  return render(request, 'register.html')
  
def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user = form.get_user()  # Get the authenticated user from the form
            auth_login(request, user)  # Log the user in
            return redirect('profile')  # Redirect to the home page or any other page
        else:
            return render(request, 'login.html', {'form': form, 'error': 'Username or password is incorrect.'})

    form = AuthenticationForm()  # Initialize the form for GET request
    return render(request, 'login.html', {'form': form})
@login_required     
def profile_page(request):
    return render(request, 'profile.html', {'user': request.user})

def logout_page(request):
    # Log the user out and clear session data
    auth_logout(request)
    request.session.flush()
    #Session.objects.filter(session_key=request.session.session_key).delete()
    #response.delete_cookie('sessionid')
    return redirect('home')
     
    
#for debugging perpose
"""
def logout_page(request):
    logger.info(f"Session before logout: {request.session.items()}")
    auth_logout(request)  # Logs out the user
    request.session.flush()  # Clears session data
    Session.objects.filter(session_key=request.session.session_key).delete()  # Manually remove session data from DB
    logger.info(f"Session after flush: {request.session.items()}")
    response = redirect('login')  # Redirect to the login page
    response.delete_cookie('sessionid')  # Remove session cookie
    logger.info(f"User after logout: {request.user}")
    return response

def profile_page(request):
    print(f"Session ID: {request.session.session_key}", flush=True)
    if request.user.is_authenticated:
        return render(request, 'profile.html', {'user': request.user})
    return redirect('login')
    
"""
