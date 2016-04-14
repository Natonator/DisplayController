from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,"displayController/home.html", {'home': "Welcome home!"})
    # return render_to_response("displayController/home.html", {'home': "Welcome home!"})
def slideshow(request):
    return render(request, "displayController/slideshow.html", {'home': "A slideshow"})

def menu(request):
    return render(request, "displayController/menu.html", {'home': "A menu"})
