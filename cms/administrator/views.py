from django.shortcuts import render, render_to_response
from django.http import HttpResponse
# from django.template import RequestContext
from django.http import HttpResponseRedirect
# from .forms import LoginForm
from django.forms import formset_factory
from .forms import *
from .models import *


def informationEdit(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            form = informationForm(request.POST, request.FILES)
            if form.is_valid():
                if information.objects.filter(pk=1).exists():
                    info = information.objects.get(pk=1)
                    info.title = form.cleaned_data['title']
                    info.body = form.cleaned_data['body']
                    info.img = form.cleaned_data['img']
                else:
                    info = information(title = form.cleaned_data['title'], body=form.cleaned_data['body'], img=form.cleaned_data['img'])
                info.save()
                return render(request, "administrator/test.html", {'model':info})
            else:
                return render(request, "administrator/fail.html", {'errors': form.errors})
        else:
            if information.objects.filter(pk=1).exists():
                info = information.objects.get(pk=1)
            else:
                info = False
            if info:
                #fill the form information
                form = informationForm(initial={'title':info.title, 'body':info.body})
            else:
                form = informationForm()
            return render(request, "administrator/informationEdit.html", {'form': form, 'info': info})
    else:
        return HttpResponseRedirect('/')


def menuEdit(request):
    if request.user.is_authenticated():
        #get all of the menu items
        if request.method == 'POST':
            formset = formset_factory(request.POST)
            if formSet.is_valid():
                return render(request, "administrator/test.html")
            else:
                return render(request, "administrator/fail.html", {'errors': formSet.errors})
        else:
            formSet = formset_factory(menuForm, extra=5)
            return render(request, "administrator/menuEdit.html", {'formSet':formSet})
    else:
        return HttpResponseRedirect('/')

def scheduleEdit(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            #process request
            form = scheduleForm(request.POST)
            if form.is_valid():
                if schedule.objects.filter(pk=1).exists():
                    scheduleModel = schedule.objects.get(pk=1)
                    scheduleModel.iframeCode = form.cleaned_data['iframeCode']
                    scheduleModel.include = form.cleaned_data['include']
                    scheduleModel.save()
                else:
                    scheduleModel = schedule(iframeCode=form.cleaned_data['iframeCode'], include=form.cleaned_data['include'])
                    scheduleModel.save()
                return render(request, "administrator/test.html", {'model': scheduleModel})
            else:
                return render(request, "administrator/fail.html", {'errors': form.errors})
        else:
            # form = scheduleForm()
            if schedule.objects.filter(pk=1).exists():
                scheduleModel = schedule.objects.get(pk=1)
            else:
                scheduleModel = False
            if scheduleModel:
                form = scheduleForm(initial={'iframeCode':scheduleModel.iframeCode, 'include':scheduleModel.include})
            else:
                form = scheduleForm()
            return render(request, "administrator/scheduleEdit.html", {'form': form, 'schedule':scheduleModel})
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
            if displayModel.objects.filter(pk=1).exists():
                setting = schedule.objects.get(pk=1)
            else:
                setting = False
            if setting:
                form = settingsForm() #give the active one the default
            else:
                form = settingsForm()
            form.fields['view'].widget.attrs={'class':'form-control'}
            return render(request, "administrator/settings.html", {'form': form})
    else:
        # Do something for anonymous users.
        return HttpResponseRedirect('/')

def slideshowEdit(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            slideShowFormSet = formset_factory(SlideShowForm)
            slideFormSet  = slideShowFormSet(request.POST, request.FILES)
            if slideFormSet.is_valid():
                for index, form in enumerate(slideFormSet):
                    # index = str(index)
                    index = index
                    # pk_index = 'form-'+index+'-pkId'
                    primaryk = slideFormSet.cleaned_data[index]['pkId']
                    # primaryk = slideFormSet
                    # return render(request, "administrator/test.html", {'info':primaryk})
                    if primaryk > 0:
                        if slideshow_images.objects.filter(pk=int(primaryk)).exists():
                            tempModel = slideshow_images.objects.get(pk=int(primaryk))
                            tempModel.fileName = slideFormSet.cleaned_data[index]['fileName']
                            tempModel.image_include = slideFormSet.cleaned_data[index]['image_include']
                            tempModel.alt = slideFormSet.cleaned_data[index]['alt']
                            tempModel.sort = slideFormSet.cleaned_data[index]['sort']
                            tempModel.save()
                    else:
                        tempModel = slideshow_images(
                            fileName = slideFormSet.cleaned_data[index]['fileName'],
                            image_include = slideFormSet.cleaned_data[index]['image_include'],
                            alt = slideFormSet.cleaned_data[index]['alt'],
                            sort = slideFormSet.cleaned_data[index]['sort'],
                        )
                        tempModel.save()
                return render(request, "administrator/test.html", {'info':"hello nate"})
            else:
                return render(request, "administrator/fail.html", {'errors': slideFormSet.errors})
        else:
            # if slideshow_images.objects.all().count() > 0
            imgs = slideshow_images.objects.all()
            slideShowFormSet = formset_factory(SlideShowForm, extra=imgs.count() + 1, max_num=9)
            # fill the defualt data
            slideFormSet = slideShowFormSet(initial=[
                {fileName : img.fileName},
                {image_include : img.image_include},
                {alt : img.alt},
                {sort : img.sort},
                {pkId : img.id}
                for img in imgs])
            return render(request, "administrator/slideshowEdit.html", {'formset': slideFormSet, 'models':imgs})
    else:
        return HttpResponseRedirect('/')
