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
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()  # Get the authenticated user from the form
            auth_login(request, user)  # Log the user in
            return redirect('home')  # Redirect to the home page or any other page
        else:
            return render(request, 'login.html', {'form': form, 'error': 'Username or password is incorrect.'})

    form = AuthenticationForm()  # Initialize the form for GET request
    return render(request, 'login.html', {'form': form})
    
@login_required
def profile_page(request):
    if not request.user.is_authenticated:
       return redirect('home')  # Redirect to login page if the user is not authenticated
    
    return render(request, 'profile.html', {'user': request.user})

def logout_page(request):
    # Log the user out and clear session data
    auth_logout(request)
    request.session.flush()  # Clears session data

    # Create the response object to send back to the client
    response = redirect('home')

    # Delete the session cookie from the browser
    response.delete_cookie('sessionid')  # Remove the default session cookie

    # Optionally delete other cookies (e.g., CSRF token or custom cookies)
    response.delete_cookie('csrftoken')  # Remove CSRF token cookie
    # If you have any custom cookies, delete them here as well
    # response.delete_cookie('your_custom_cookie_name')

    return response
    
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