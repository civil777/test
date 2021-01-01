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


class Photo1(core_models.TimeStampedModel):
    """ Photo Model Definition"""

    files = models.ImageField(upload_to="product_photos1")
    places = models.ForeignKey('Rooma', related_name="home", on_delete=models.CASCADE)


class Rooma(core_models.TimeStampedModel):
    """ Room Model Definition """

    name = models.CharField(max_length=100, verbose_name='제목')

    address = models.CharField(max_length=140, verbose_name='주소')

    host = models.ForeignKey("users.User", related_name="home", on_delete=models.CASCADE, verbose_name='담당자', blank=True, null=True)

    def __str__(self):
        return self.name

    def first_photo(self):
        try:
            photo, = self.home.all()[:1]
            return photo.files.url
        except ValueError:
            return None

    class Meta:
        verbose_name = '메인화면 현장사례'
        verbose_name_plural = '메인화면 현장사례'


class Jquestion(core_models.TimeStampedModel):
    subject = models.CharField(max_length=20)
    content = models.TextField()


    def __str__(self):
        return self.subject


class Answer(models.Model):
    question = models.ForeignKey(Jquestion, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()


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


class Naver(models.Model):
    pass
