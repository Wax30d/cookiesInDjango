from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def setcookie(request):
    html = HttpResponse("<h1>Django Tutorial</h1>")
    html.set_cookie('From Cooker Wax30d', 'Hello this is your Cookies', max_age=None)
    return html
