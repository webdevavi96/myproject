from django.shortcuts import render

# Create your views here.

def index(request):
   	 return render(request, 'index.html')
   	 
def home(request):
   	 return render(request, 'home.html')
   	 
def about(request):
   	 return render(request, 'about.html')  
   	 
def ourteam(request):
   	 return render(request, 'ourteam.html')   
   	
def gallery(request):
   	 return render(request, 'gallery.html')   	 
   	 
def notes(request):
   	 return render(request, 'notes.html')   	 
   	 
def registration(request):
   	 return render(request, 'registration.html') 
   	 
def contactus(request):
   	 return render(request, 'contactus.html')   
   	 
def joinus(request):
   	 return render(request, 'joinus.html')   	 
   	 