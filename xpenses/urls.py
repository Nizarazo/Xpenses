"""xpenses URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
import random

from django.conf.urls import url
from django.contrib import admin
from django.http import HttpResponse
from django.http import JsonResponse


def home(request):  # view function
    # assert False, "KABOOM!!!!"
    return HttpResponse("Hello <b>World!</b>")


def lucky(request):
    return JsonResponse({
        'lucky': random.randint(1, 10),
    })


def hello(request, name):  # view function
    return HttpResponse("Hello <b>{}</b>".format(
        name.title(),
    ))


urlpatterns = [
    url(r'^$', home),
    url(r'^api/$', lucky),
    url(r'^hello/([a-zA-Z]+)/$', hello),
    url(r'^admin/', admin.site.urls),
]
