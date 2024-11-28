import os
from lib2to3.fixes.fix_input import context
from uuid import uuid4
from django.conf import settings
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Feed
from djangoProject.settings import MEDIA_ROOT

# Create your views here.


class Main(APIView):
    def get(self, request):
        feed_list = Feed.objects.all().order_by('-id') # == select * from content_feed;

        return render(request, "jeongstagram/main.html", context=dict(feeds=feed_list)) # render(request, url, arg)
    #render를 사용하면 페이지 전체가 로딩되는 것
    #ajax를 사용하면 비동기 처리로 일부만 로딩되는 것

    #피드 올리기


class UploadFeed(APIView):
    def post(self, request):

        file = request.FILES['file'] #파일 불러와

        uuid_name = uuid4().hex #서버에 올릴때는 이미지의 이름을 uuid함수를 사용하여 고유의 이름값을 줌(한글 등의 경우 오류가 날 수있기 때문)
        save_path = os.path.join(MEDIA_ROOT, uuid_name) # ~/PycharmProjects/Jeongstargram/media + uuid_name

        with open(save_path, 'wb+') as destination: #파일을 읽고 저장할때 사용하는 코드
            for chunk in file.chunks():
                destination.write(chunk)

        image = uuid_name
        content = request.data.get('content')
        user_id = request.data.get('user_id')
        profile_image = request.data.get('profile_image')

        Feed.objects.create(image=image, content=content, user_id=user_id, profile_image=profile_image, like_count =0)

        # print(file)
        # print(image)

        return Response(status=200) #httpResponse
