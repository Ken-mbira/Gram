from django.shortcuts import render,redirect
from .models import Profile
from django.contrib import messages

from .forms import UpdateProfileForm

# Create your views here.
def home(request):
    """This will render the home page

    Args:
        request ([type]): [description]
    """
    if request.user.is_authenticated:
        return render(request,'gram/index.html')
    else:
        return redirect('login')

def user_profile(request,pk):
    """This will manage the user profile page

    Args:
        request ([type]): [description]
    """
    user = request.user
    try:
        profile = Profile.objects.get(user = user)
        return render(request,'gram/profile.html',{"profile":profile})

    except :
        messages.success(request,'Sorry, but it seems your profile page is not set up, you could do so here!')
        return redirect('update_profile')
        
def update_profile(request):
    """This will manage the update of data into the profile

    Args:
        request ([type]): [description]
    """
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST,request.FILES,instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile',request.user.pk)
        else:
            messages.success(request,'There was a problem with your profile form')
            return render(request,'gram/update_profile.html',{"form":form})
            


    else:
        form = UpdateProfileForm(instance=request.user.profile)
        return render(request,'gram/update_profile.html',{"form":form})

def post(request,pk):
    """This will handle a new post

    Args:
        request ([type]): [description]
    """
    return render(request,'gram/add_post.html')