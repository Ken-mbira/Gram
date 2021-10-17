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
    profile_pic = models.ImageField(null=True,blank=True,upload_to='profile/')

    def save_profile(self):
        """This will save a profile to the database
        """
        self.save()

    def delete_profile(self):
        """This will remove a profile from the database
        """
        self.delete()

    def update_profile(self,new):
        """This will update a user's profile

        Args:
            new ([type]): [description]
        """
        self.username = new.username
        self.bio = new.bio
        self.profile_pic = new.profile_pic
        self.save()