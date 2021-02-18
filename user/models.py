from django.db import models

from django.contrib.auth.models import AbstractUser, UserManager


# AbstractUser는 이미 username, email, password, first_name, last_name 같은 필드를 갖고 있음

class CustomUser(AbstractUser):
    objects = UserManager()

    nickname = models.CharField(max_length=10, blank=True)
    introduction = models.CharField(max_length=100, blank=True)
    profile_image = models.ImageField(blank=True, null=True, upload_to="profile", verbose_name = '이미지')