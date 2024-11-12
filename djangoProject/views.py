from rest_framework.views import APIView
from django.shortcuts import render

# django rest framework 다운로드 해야 restful 사용
class Sub(APIView):
    def get(self, request):
        return render(request, "jeongstagram/main.html")
