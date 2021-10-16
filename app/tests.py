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

    # def tearDown(self):
    #     """This will clear the database after every test case
    #     """
    #     self.user.delete()