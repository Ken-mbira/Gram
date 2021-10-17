from django.test import TestCase

# Create your tests here.
from .models import Profile,Image
from django.contrib.auth.models import User

class TestProfile(TestCase):
    """This tests the behaviours of the profile class

    Args:
        TestCase ([type]): [description]
    """
    def setUp(self):
        """This will run before every test case
        """
        self.user = User.objects.create(username='mbira')
        self.user.save()
        self.user_profile = Profile(user = self.user,username='kenmbesh',bio='my bio',profile_pic='image')

    def test_instance(self):
        self.assertTrue(isinstance(self.user_profile,Profile))

    def test_save_profile(self):
        """This will check if a profile can be saved to the database
        """
        self.user_profile.save_profile()
        profiles = Profile.objects.all()

        self.assertTrue(len(profiles)>0)

    def test_delete_profile(self):
        """This will check that a profile can be deleted from the database
        """
        self.user_profile.save_profile()
        self.user_profile.delete_profile()
        profiles = Profile.objects.all()

        self.assertTrue(len(profiles) == 0)

    def test_update_profile(self):
        """This will test that we can update a profile
        """
        self.user_profile.save_profile()
        new = Profile(user = self.user,username = 'Kinyanjui',bio="hello",profile_pic='another location')

        self.user_profile.update_profile(new)
        self.assertTrue(self.user_profile.username == 'Kinyanjui')

    def test_search_by_username(self):
        """This will check if one can user a username to retrieve profiles from the datbase
        """
        self.user_profile.save_profile()
        term = 'ken'
        found_profiles = self.user_profile.search_profile(term)

        self.assertEqual(found_profiles[0].username,self.user_profile.username)

class TestImage(TestCase):
    """This will define the behaviours of the image class

    Args:
        TestCase ([type]): [description]
    """
    def setUp(self):
        """This runs before every test
        """
        self.user = User.objects.create(username='mbira')
        self.user.save()

        self.image = Image(user = self.user,image_path = 'blah',image_caption = 'blah',likes = 1)

    def test_instance(self):
        """This tests whether an image instance can be created
        """
        self.assertTrue(isinstance(self.image,Image))

    def test_save_image(self):
        """This will check if an image can be saved to the database
        """
        self.image.save_image()
        images = Image.objects.all()

        self.assertTrue(len(images)>0)

    def test_delete_image(self):
        """This will check that an image can get deleted
        """
        self.image.save_image()
        self.image.delete_image()
        images = Image.objects.all()

        self.assertTrue(len(images) == 0)

    def test_update_image_caption(self):
        """This will test that an image caption can be updated
        """
        self.image.save_image()
        new_caption = 'This is a new image caption'

        self.image.update_caption(new_caption)

        self.assertTrue(self.image.image_caption == new_caption)
