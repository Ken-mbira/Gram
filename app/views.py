from django.shortcuts import render

# Create your views here.
def home(request):
    """This will render the home page

    Args:
        request ([type]): [description]
    """
    message = 'Hello world!'
    return render(request,'gram/index.html',{'message':message})
