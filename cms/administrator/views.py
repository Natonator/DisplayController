from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from .forms import LoginForm

def login(request):
    if request.method == 'POST':
        form = LoginForm(request)
        if form.is_valid():
            print "it worked"
    else:
        form = LoginForm
    return render(request, "administrator/login.html", {'form': form})
