from django.db import models
from core import models as core_models


class Question(core_models.TimeStampedModel):

    이름 = models.CharField(max_length=10, blank=True, default="")
    전화번호 = models.CharField(max_length=13, blank=True, default="")
    이메일 = models.CharField(max_length=50, blank=True, default="")
    주소 = models.CharField(max_length=50, blank=True, default="")
    문의사항 = models.TextField(blank=True, default="")



class Index(models.Model):
    text = models.TextField(default="")

class Test(models.Model):
    text = models.TextField(default="")
