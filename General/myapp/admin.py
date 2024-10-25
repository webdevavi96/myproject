from django.contrib import admin
from .models import User  # Update the import statement

admin.site.register(User)  # Register the renamed model
