from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

# Create your models here.
class User(AbstractBaseUser):
    """
        유저 프로필 사진
        유저 닉네임
        유저 이메일 주소(회원가입시)
        유저 비밀번호 --> 상속받는 제공 유저의 디폴트 함수 쓸 예정
        유저 실명
    """
    profile_image = models.TextField()  # 프로필 이미지
    nickname = models.CharField(max_length=24,unique=True)
    name = models.CharField(max_length=24)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'nickname'   #유저이름을 어떤걸로 쓸 건지(unigue)


    class Meta:
        #테이블 이름 정할 수 있음
        db_table = 'User'