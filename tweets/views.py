from django.shortcuts import render

# Create your views here.


def home_view(request, **args, **kwags):
    return HttpResponse("<h1>Hello</h1>")
