from django.contrib import admin
from . import models
from django.utils.html import mark_safe



class PhotoInline(admin.TabularInline):

    model = models.Photo
    fk_name = "place"

@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    inlines = (PhotoInline,)

    list_display = (
        "name",
    )
    seaerch_fields = ("name", "^host__username",)

    raw_id_fields = ("host",)

@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="70px" src="{obj.file.url}" />')