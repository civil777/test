from django.db import models
from core import models as core_models


class Question(core_models.TimeStampedModel):

    이름 = models.CharField(max_length=10, blank=True, default="")
    전화번호 = models.CharField(max_length=13, blank=True, default="")
    이메일 = models.CharField(max_length=50, blank=True, default="")
    주소 = models.CharField(max_length=50, blank=True, default="")
    문의사항 = models.TextField(blank=True, default="")

    class Meta:
        verbose_name = '문의사항'
        verbose_name_plural = '문의사항'



class Index(models.Model):
    text = models.TextField(default="")

class Test(models.Model):
    pass

class T1(models.Model):
    pass

class T2(models.Model):
    pass

class T3(models.Model):
    pass

class T4(models.Model):
    pass

class T5(models.Model):
    pass

class Q1(models.Model):
    pass

class Q2(models.Model):
    pass

class W1(models.Model):
    pass
class W2(models.Model):
    pass