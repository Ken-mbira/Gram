from django.shortcuts import render

# Create your views here.
def user_login(request):
    """This will render the login page

    Args:
        request ([type]): [description]
    """
    message = "login"
    return render(request,'authenticate/login.html',{'message':message})
