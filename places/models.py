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

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    host = models.ForeignKey("users.User", related_name="places", on_delete=models.CASCADE)
    special_item = models.BooleanField(default=False)
    time = models.TimeField()
    item_type = models.ForeignKey("RoomType", related_name="places", on_delete=models.SET_NULL, null=True)

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

    def get_next_four_photos(self):
        photos = self.photos.all()[1:5]
        return photos

    def all_product(self):
        product, = self.photos.all()
        return product.file.url



