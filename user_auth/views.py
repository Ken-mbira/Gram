from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages

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
