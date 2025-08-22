from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    bio = models.TextField(max_length=500, blank=True, help_text="User biography")
    profile_picture = models.ImageField(
        upload_to='profile_pic',
        blank=True,
        null=True,
        help_text="User profile picture"
 )
    followers = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='following',
        help_text="Users who follow this user"
    
    )
    def __str__(self):
        return self.username
    
    @property
    def followers_count(self):
        return self.followers.count()
    
    @property
    def following_count(self):
        return self.following.count()
    


