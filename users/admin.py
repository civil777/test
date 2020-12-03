from django.contrib import admin
from . import models

@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("username", "전화번호", "주소","문의사항" )

