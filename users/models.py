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
        #default='https://placehold.co/40x40/4f46e5/ffffff?text={{ user.username|first|upper',
        upload_to='profile_pics/',
        force_format='WEBP',
        blank=True,
        null=True
    )

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        # Check if this is an existing instance
        if self.pk:
            try:
                old_instance = UserProfile.objects.get(pk=self.pk)
                # If the profile picture has changed and the old one is not the default
                if old_instance.profile_picture != self.profile_picture:
                    if old_instance.profile_picture and old_instance.profile_picture.name != 'profile_pics/default.jpg':
                        old_instance.profile_picture.delete(save=False)
            except UserProfile.DoesNotExist:
                pass # Should not happen, but good to be safe
        super().save(*args, **kwargs)
    
