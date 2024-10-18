from django.shortcuts import render
   	 
   	 # Create your views here.
   	 
def index(request):
    return render(request, 'index.html')
   	 
def home(request):
    return render(request, 'home.html')
   	 
def about(request):
    return render(request, 'about.html')
   	 
def places(request):
    return render(request, 'places.html')
   	 
def gallery(request):
    return render(request, 'gallery.html')
   	 
   	 
def booking(request):
    return render(request, 'booking.html')
    
def contactus(request):
   	return render(request, 'contactus.html')
   	 
def joinus(request):
    return render(request, 'joinus.html')
   	 