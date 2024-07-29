from django.db import models
from django.contrib.auth.models import User
from django.core.validators import EmailValidator, MinLengthValidator

class Professional(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='professional_profile')
    email = models.EmailField(max_length=254, blank=True, validators=[EmailValidator()])
    city = models.CharField(max_length=120, blank=True)
    profession = models.CharField(max_length=120, blank=True)
    skills = models.TextField(blank=True, help_text="Comma-separated skills list")
    profile_picture = models.ImageField(upload_to='profilepics/', blank=True, null=True)
    joining_date = models.DateField(auto_now_add=True)
    bio = models.TextField(blank=True, help_text="Brief biography")
    phone_number = models.CharField(max_length=15, blank=True)
    website = models.URLField(blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.profession}"

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='client_profile')
    email = models.EmailField(max_length=254, blank=True, validators=[EmailValidator()])
    city = models.CharField(max_length=120, blank=True)
    profile_picture = models.ImageField(upload_to='profilepics/', blank=True, null=True)
    joining_date = models.DateField(auto_now_add=True)
    phone_number = models.CharField(max_length=15, blank=True)
    bio = models.TextField(blank=True, help_text="Brief biography")

    def __str__(self):
        return f"{self.user.username} - Client"
