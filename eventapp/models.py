from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    venue = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    bookng_last_date = models.DateTimeField()
    arrival_date = models.DateTimeField()
    end_date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "events")
    
    def __str__(self):
        return self.title
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, max_length=150)
    location = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=14)
    
    def __str__(self):
        return f"{self.user.username}'s prfile"