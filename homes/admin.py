from django.contrib import admin
from . import models

@admin.register(models.Question)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("이름", "전화번호", "주소", "문의사항", "created", )

class PhotoInline(admin.TabularInline):

    model = models.Photo1
    fk_name = "places"

@admin.register(models.Rooma)
class RoomAdmin(admin.ModelAdmin):

    inlines = (PhotoInline,)

    list_display = (
        "name",
    )

    raw_id_fields = ("host",)

@admin.register(models.Jquestion)
class JquAdmin(admin.ModelAdmin):

    list_display = ("subject", "created", )

@admin.register(models.Answer)
class JanswerAdmin(admin.ModelAdmin):

    list_display = ("question", "create_date", "content", )
