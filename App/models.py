from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Professionals(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    email = models.CharField(max_length=120,blank=True)
    city = models.CharField(max_length=120,blank=True)
    profession = models.CharField(max_length=120,blank=True)
    skills = models.TextField(blank=True)
    profile_picture = models.ImageField( upload_to='profilepics/')
    joining_date= models.DateField()
    
    def __str__(self):
        return self.user.username
    
    

class Clients(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    email = models.CharField(max_length=120,blank=True)
    city = models.CharField(max_length=120,blank=True)
    profile_picture = models.ImageField( upload_to='profilepics/')
    joining_date= models.DateField()
    
    def __str__(self):
        return self.user.username
    
