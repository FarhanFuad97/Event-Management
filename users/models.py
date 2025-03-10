from django.db import models

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    profile_image = models.ImageField(upload_to="profile_images/", blank=True, default='profile_images/Default.jpg')
    phone = models.CharField(max_length=15, blank=True, null=True) 

    def __str__(self):
        return self.username



    


