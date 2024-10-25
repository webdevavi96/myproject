from django.db import models

class CustomUser(models.Model):  # Make sure this is your model name
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name
