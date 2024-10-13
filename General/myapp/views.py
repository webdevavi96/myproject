from django.shortcuts import render
   	 
   	 def render_template(request, template_name):
   	     return render(request, template_name)
   	 
   	 def index(request):
   	     return render_template(request, 'index.html')
   	 
   	 def home(request):
   	     return render_template(request, 'home.html')
   	 
   	 def about(request):
   	     return render_template(request, 'about.html')
   	 
   	 def ourteam(request):
   	     return render_template(request, 'ourteam.html')
   	 
   	 def gallery(request):
   	     return render_template(request, 'gallery.html')
   	 
   	 def notes(request):
   	     return render_template(request, 'notes.html')
   	 
   	 def registration(request):
   	     return render_template(request, 'registration.html')
   	 
   	 def contactus(request):
   	     return render_template(request, 'contactus.html')
   	 
   	 def joinus(request):
   	     return render_template(request, 'joinus.html')
   	 