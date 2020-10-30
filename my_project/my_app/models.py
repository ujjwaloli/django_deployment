from django.db import models
from django.contrib.auth.models import User

#SuperUserInformation
#User: Ujjwal
#Email: ujjwaloli22@gmail.com
#Password: testpassword

# Create your modles here.

class UserProfileInfo(models.Model):

    # Create relationship (don't inherit from User!)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Add any additional attributes you want
    portfolio_site = models.URLField(blank=True)
    # pip install pillow to use this
    profile_pic = models.ImageField(upload_to='my_app/profile_pics', blank=True)

    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User
        return self.user.username
