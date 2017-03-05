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
import calendar
import random

from django.conf.urls import url
from django.contrib import admin
from django.http import HttpResponse
from django.http import JsonResponse


def home(request):  # view function
    # assert False, "KABOOM!!!!"
    return HttpResponse("Hello <b>World!</b>")


def add(request, x, y):
    return HttpResponse("{} + {} = <b>{}</b>".format(
        x, y, int(x) + int(y)
    ))


def hello_lucky(request, name, number):
    return HttpResponse(
        "Hello <b>{}</b> Your lucky number is <b>{}</b>".format(
            name.title(),
            number,
        ))


urlpatterns = [
    url(r'^$', home),
    url(r'^add/([0-9]+)/([0-9]+)/$', add),
    url(r'^hello/([a-zA-Z]+)/$', hello_lucky, kwargs={'number': 99}),
    url(r'^hello/([a-zA-Z]+)/([0-9]+)/$', hello_lucky),
    url(r'^hello/(?P<number>[0-9]+)/(?P<name>[a-zA-Z]+)/$', hello_lucky),
    url(r'^admin/', admin.site.urls),
]
