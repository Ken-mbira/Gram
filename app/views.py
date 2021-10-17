from django.shortcuts import render,redirect
from .models import Image, Profile
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import UpdateProfileForm,CreatePostForm

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
        posts = Image.objects.filter(user = request.user)
        return render(request,'gram/profile.html',{"profile":profile,"posts":posts})

    except Exception as e:
        print(e)
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
    if request.method == 'POST':
        form = CreatePostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"Your post has been created successfully!")
        return redirect('home')
    else:
        form = CreatePostForm(initial={'user':request.user})
        return render(request,'gram/add_post.html',{'form':form})

def search_profile(request):
    """This will display the results of a search

    Args:
        request ([type]): [description]
    """
    if 'search_term' in request.GET and request.GET['search_term']:
        search_term = request.GET['search_term']
        profiles = Profile.search_profile(search_term)
        return render(request,"gram/search_results.html",{'profiles':profiles,"term":search_term})
    else:
        messages.success(request,"You have not searched for any term.")
        return HttpResponseRedirect(reverse('home'))