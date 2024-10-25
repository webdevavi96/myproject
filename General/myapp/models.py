from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    # Increase max_length to accommodate hashed passwords
    password = models.CharField(max_length=255) 

    def __str__(self):
        return self.name
