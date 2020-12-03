from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    전화번호 = models.CharField(max_length=13, default="")
    문의사항 = models.TextField(default="")
    주소 = models.CharField(max_length=100, default="")
