from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    """This will define all the components of a user's profile

    Args:
        models ([type]): [description]
    """
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    date_joined = models.DateTimeField(auto_now_add=True)
    bio = models.TextField(blank=True)
    profile_pic = models.ImageField(upload_to='profile/')




