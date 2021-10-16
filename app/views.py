from django.shortcuts import render,redirect
from django.contrib.auth import user_logged_in

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
    return render(request,'gram/profile.html')
