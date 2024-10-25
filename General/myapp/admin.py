from django.contrib import admin
from .models import User  # Ensure this matches the model name in models.py

admin.site.register(User)  # Register the User model
