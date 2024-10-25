from django.contrib import admin
from .models import CustomUser  # Update the import to CustomUser

admin.site.register(CustomUser)  # Register the CustomUser model
