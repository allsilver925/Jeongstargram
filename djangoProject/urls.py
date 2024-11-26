"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .views import Sub
from content.views import Main, UploadFeed

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/',Main.as_view()), #?
    path('content/upload', UploadFeed.as_view())
]

# 가상환경 실행 : source .venv/scripts/activate

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# 이미지파일을 media 폴더에 올려놓고 나중에 조회할 수 있도록 하는 코드
