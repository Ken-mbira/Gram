from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

from .emails import send_welcome_email
from .forms import UserRegistrationForm
from app.models import Profile

# Create your views here.
def user_login(request):
    """This will render the login page

    Args:
        request ([type]): [description]
    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request,user)
            messages.success(request,f'Welcome back {username},')
            return redirect('home')
        else:
            messages.success(request,"You have entered the wrong credentials check either your username or your password")
            return render(request,'authenticate/login.html')

    else: 
        return render(request,'authenticate/login.html')

def user_logout(request):
    """This will handle logging out a user

    Args:
        request ([type]): [description]
    """
    logout(request)
    messages.success(request,'You were logged out')
    return redirect('home')

def user_register(request):
    """This will handle registering a user to the service

    Args:
        request ([type]): [description]
    """
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email']
            send_welcome_email(username,email)

            
            user = authenticate(username=username,password=password)
            Profile.objects.create(user = user)

            login(request,user)
            messages.success(request,f"Congratulations {username}, your account was successfully created!")
            return redirect('home')

        else:
            messages.success(request,'There was a problem with your form, you could check if your username has spaces')
            form = UserRegistrationForm()
            return render(request,'authenticate/register.html',{"form":form})

    else:
        form = UserRegistrationForm()
        return render(request,'authenticate/register.html',{"form":form})
