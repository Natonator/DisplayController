from django import forms
from .models import *
from administrator.choices import *


class informationForm(forms.Form):
    title = forms.CharField(label="Title",max_length=20)
    body = forms.CharField(widget=forms.Textarea)
    img = forms.FileField(label='Select a file')

class menuForm(forms.Form):
    description = forms.CharField(max_length=20)
    price = forms.FloatField()
    include = forms.BooleanField()

class scheduleForm(forms.Form):
    iframeCode = forms.CharField(max_length=500)
    include = forms.BooleanField()

class settingsForm(forms.Form):
    view = forms.ChoiceField(choices=STATUS_CHOICES, label="", initial='', widget=forms.Select(), required=True)

class SlideShowForm(forms.Form):
    @property
    def __name__(self):
        return self.__class__.__name__
    #create dynamic number of choices etc like the menu
    fileName = forms.FileField(label='Select a file')
    image_include = forms.BooleanField()
    alt = forms.CharField(max_length=100)
    sort = forms.IntegerField()
    pkId = forms.IntegerField(widget=forms.HiddenInput(), initial=-1)
    # form
