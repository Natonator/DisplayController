"""cms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls import include
from django.conf.urls import patterns
from django.contrib import admin
import displayController.views
import administrator.views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout'), #shold redirect to the right url

    url(r'^information-edit/$', administrator.views.informationEdit, name='informationEdit'),
    url(r'^menu-edit/$', administrator.views.menuEdit, name='menuEdit'),
    url(r'^schedule-edit/$', administrator.views.scheduleEdit, name='scheduleEdit'),
    url(r'^settings/$', administrator.views.settings, name='setting'),
    url(r'^slideshow-edit/$', administrator.views.slideshowEdit, name='slideshowEdit'),


    url(r'^$', displayController.views.home, name='home'),
    url(r'^slideshow/', displayController.views.slideshow, name='slideshow'),
    url(r'^menu/', displayController.views.menu, name='menu'),
]
