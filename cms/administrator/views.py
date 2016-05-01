from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import LoginForm


def informationEdit(request):
    if request.user.is_authenticated():
        #load the saved information
        #load the path of the Images
        #load the title
        return render(request, "administrator/informationEdit.html")
    else:
        return HttpResponseRedirect('/')


def menuEdit(request):
    if request.user.is_authenticated():
        #get all of the menu items
        return render(request, "administrator/menuEdit.html")
    else:
        return HttpResponseRedirect('/')

def scheduleEdit(request):
    if request.user.is_authenticated():
        #get the google token
        #get the calendar url
        return render(request, "administrator/scheduleEdit.html")
    else:
        return HttpResponseRedirect('/')

def settings(request):
    if request.user.is_authenticated():
        return render(request, "administrator/settings.html")
    else:
        # Do something for anonymous users.
        return HttpResponseRedirect('/')

def slideshowEdit(request):
    if request.user.is_authenticated():
        #get the paths of all the images
        #get all alt tabs
        #get display order
        return render(request, "administrator/slideshowEdit.html")
    else:
        return HttpResponseRedirect('/')
