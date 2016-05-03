from django import forms
# from PIL import Image
from administrator.choices import *


class informationForm(forms.Form):
    title = forms.CharField(label="Title",max_length=20)
    body = forms.CharField(widget=forms.Textarea)
    img = forms.FileField(label='Select a file') # files are not validating

# class menuForm(forms.Form):
#     #need to make this dynamic
#     #look at model choice field
#     description = forms.CharField(max_length=20)
#     price = forms.FloatField()
#     include = forms.BooleanField()

class scheduleForm(forms.Form):
    calendar= forms.URLField()
    api_key = forms.CharField(max_length=32)

class settingsForm(forms.Form):
    view = forms.ChoiceField(choices=STATUS_CHOICES, label="", initial='', widget=forms.Select(), required=True)

# class SlideShowForm(forms.Form):
#     #create dynamic number of choices etc like the menu
#     order = forms.IntegerField()
#     # form
