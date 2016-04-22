from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from .forms import LoginForm

def login(request):
    form = LoginForm(request)
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        print username
        print password
        # if form.is_valid():
        #     print "it worked"
    else:
        form = LoginForm
    return render(request, "administrator/login.html", {'form': form})
