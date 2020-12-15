from django.utils import timezone
from django.db import models
from django.urls import reverse
from core import models as core_models


class AbstractItem(core_models.TimeStampedModel):
    """ Abstract Item"""

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):
    pass


class Photo(core_models.TimeStampedModel):
    """ Photo Model Definition"""

    file = models.ImageField(upload_to="product_photos")
    place = models.ForeignKey('Room', related_name="photos", on_delete=models.CASCADE)


class Room(core_models.TimeStampedModel):
    """ Room Model Definition """

    name = models.CharField(max_length=100, verbose_name='제목')
    description = models.TextField(verbose_name='상세설명', default="", null=True)

    address = models.CharField(max_length=140,  verbose_name='주소')
    host = models.ForeignKey("users.User", related_name="places", on_delete=models.CASCADE,  verbose_name='담당자')
    
    time = models.DateField()
    item_type = models.ForeignKey("RoomType", related_name="places", on_delete=models.SET_NULL, null=True,  verbose_name='공법종류')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("places:detail", kwargs={"pk": self.pk})


    def first_photo(self):
        try:
            photo, = self.photos.all()[:1]
            return photo.file.url
        except ValueError:
            return None

    def second_photo(self):
        try:
            photoss, = self.photos.all()[1:2]
            return photoss.file.url
        except ValueError:
            return None

    def get_next_four_photos(self):
        photos = self.photos.all()[1:4]
        return photos

    def all_product(self):
        products = self.photos.all()[4:]
        return products

    class Meta:
        verbose_name = '현장사례'
        verbose_name_plural = '현장사례'

