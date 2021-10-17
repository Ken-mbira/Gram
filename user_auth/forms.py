from typing import Sequence
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class UserRegistrationForm(UserCreationForm):
    """This defines all the fields we're going to add in our user registration form

    Args:
        UserCreationForm ([type]): [description]
    """
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username','email','password1','password2')