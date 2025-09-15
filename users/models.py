from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    zip_code = models.CharField(max_length=10, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)

    profile_picture = ResizedImageField(
        size=[128, 128],
        quality=75,
        default='profile_pics/default.jpg',
        upload_to='profile_pics/',
        force_format='WEBP',
        blank=True,
        null=True
    )

    def __str__(self):
        return f'{self.user.username} Profile'
    
