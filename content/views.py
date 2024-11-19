from lib2to3.fixes.fix_input import context

from django.shortcuts import render
from rest_framework.views import APIView
from .models import Feed

# Create your views here.


class Main(APIView):
    def get(self, request):
        feed_list = Feed.objects.all().order_by('-id') # == select * from content_feed;

        return render(request, "jeongstagram/main.html", context=dict(feeds=feed_list)) # render(request, url, arg)