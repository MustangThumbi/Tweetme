from django.http.response import HttpResponse
from django.shortcuts import render

from .models import Tweet
# Create your views here.


def home_view(request, *args_kwags):
    return HttpResponse("<h1>Hello</h1>")


def tweet_details_view(request, tweet_id, *args_kwargs):
    obj = Tweet.objects.get(id=tweet_id)
    return HttpResponse(f"<h1> Hello {tweet_id} - {obj.content}</h1>")
