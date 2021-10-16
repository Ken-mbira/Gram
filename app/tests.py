from django.test import TestCase

# Create your tests here.
from .models import Profile
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


    # def tearDown(self):
    #     """This will clear the database after every test case
    #     """
    #     self.user.delete()