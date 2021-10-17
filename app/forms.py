from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User

from .models import Profile

class UpdateProfileForm(ModelForm):
    """This will define the fields in the profile form
    """
    class Meta:
        model = Profile
        fields = ('user','username','bio','profile_pic')
        exclude = ['user']