from django.shortcuts import render, render_to_response
from django.http import HttpResponse
# from django.template import RequestContext
from django.http import HttpResponseRedirect
# from .forms import LoginForm
from .forms import *


def informationEdit(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            #process request
            form = informationForm(request.POST, request.FILES)
            if form.is_valid():
                #select the model values
                return render(request, "administrator/test.html")
            else:
                return render(request, "administrator/fail.html", {'errors': form.errors})
        else:
            form = informationForm()
            #load the saved information
            #load the path of the Images
            #load the title
            return render(request, "administrator/informationEdit.html", {'form': form})
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
        if request.method == 'POST':
            form = settingsForm(request.POST)
            if form.is_valid():
                #select the model values
                return render(request, "administrator/test.html")
        else:
            form = settingsForm()
            form.fields['view'].widget.attrs={'class':'form-control'}
            return render(request, "administrator/settings.html", {'form': form})
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
