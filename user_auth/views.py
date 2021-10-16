from django.shortcuts import render

# Create your views here.
def user_login(request):
    """This will render the login page

    Args:
        request ([type]): [description]
    """
    return render(request,'authenticate/login.html')
