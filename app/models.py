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
    followers = models.ManyToManyField(User,related_name='followers',blank=True)

    def __str__(self):
        return self.username

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

    def search_profile(self,search_term):
        """This will return a series of profiles with a provided search term

        Args:
            search_term ([type]): [description]

        Returns:
            [type]: [description]
        """
        profiles = Profile.objects.filter(username__icontains = search_term)

        return profiles

class Image(models.Model):
    """This will define all the behaviours of an image post

    Args:
        models ([type]): [description]
    """
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    image_path = models.ImageField(null=True,blank=True,upload_to='posts/')
    image_name = models.CharField(max_length=50)
    image_caption = models.TextField(null=True,blank=True)
    likes = models.IntegerField(null=True,blank=True,default=0)
    date_added = models.DateTimeField(null=True,auto_now_add=True)

    def __str__(self):
        return self.image_name

    def save_image(self):
        """This will add the image to the database
        """
        self.save()

    def delete_image(self):
        """This will remove an image instance from the database
        """
        self.delete()

    def update_caption(self,caption):
        """This will update the image caption saved in the database

        Args:
            caption ([type]): [description]
        """
        self.image_caption = caption
        self.save()

class Comments(models.Model):
    """This defines the characteristics of a comment

    Args:
        models ([type]): [description]
    """
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ForeignKey(Image,on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self):
        return self.comment