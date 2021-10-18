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

    def total_followers(self):
        """This counts the number of followers in the profile
        """
        return self.followers.count()

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

    @classmethod
    def get_following(cls,user):
        """This will return all the users which a user is following

        Returns:
            [type]: [description]
        """
        following = user.followers.all()
        users = []
        for profile in following:
            user = User.objects.get(profile = profile)
            users.append(user)

        return users

    @classmethod
    def search_profile(cls,search_term):
        """This will return a series of profiles with a provided search term

        Args:
            search_term ([type]): [description]

        Returns:
            [type]: [description]
        """
        profiles = cls.objects.filter(username__icontains = search_term)

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
    likes = models.ManyToManyField(User,related_name="likers",blank=True)
    date_added = models.DateTimeField(null=True,auto_now_add=True)

    def __str__(self):
        return self.image_name

    def like_image(self,user):
        """This will add a user as a liker of an image
        """
        self.likes.add(user)

    def get_likes_total(self):
        """This will return the number of likes of a particular post
        """
        return self.likes.count()



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

    @classmethod
    def get_images(cls,users):
        posts = []
        for user in users:
            images = Image.objects.filter(user = user)
            for image in images:
                posts.append(image)

        return posts

    def get_comments(self):
        """This will return all the comments related to a post

        Returns:
            [type]: [description]
        """
        comments = Comments.objects.filter(image = self)
        return comments

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