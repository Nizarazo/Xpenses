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


def lucky(request):
    return JsonResponse({
        'lucky': random.randint(1, 10),
    })


def hello(request, name):
    return HttpResponse("Hello <b>{}</b>".format(name.title()))


def add(request, x, y):
    return HttpResponse("{} + {} = <b>{}</b>".format(
        x, y, int(x) + int(y)
    ))


def calendar_month(request, year, month):
    # TODO: check month, year
    return HttpResponse(calendar.HTMLCalendar().formatmonth(
        int(year), int(month)
    ))


def calendar_year(request, year):
    s = " ".join('<a href="{0}/">{0}</a>'.format(i)
                 for i in range(1, 13))
    return HttpResponse(s)


urlpatterns = [
    url(r'^$', home),
    url(r'^api/$', lucky),
    url(r'^hello/([a-zA-Z]+)/$', hello),
    url(r'^add/([0-9]+)/([0-9]+)/$', add),
    url(r'^calendar/([0-9]{4})/$', calendar_year),
    url(r'^calendar/([0-9]{4})/([0-9]{1,2})/$', calendar_month),
    url(r'^admin/', admin.site.urls),
]
