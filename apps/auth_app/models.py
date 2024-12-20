from django.db import models

class UserProfile(models.Model):
    firebase_uid = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    language = models.CharField(max_length=10, default='en')
    timezone = models.CharField(max_length=50, default='UTC')

    def __str__(self):
        return self.name
