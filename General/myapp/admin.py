from django.contrib import admin
from .models import CustomUser # Update the import statement

admin.site.register(CustomUser)  # Register the renamed model
