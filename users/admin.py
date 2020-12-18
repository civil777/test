from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


class CustomUserAdmin(UserAdmin):
    model = models.User
    list_display = ("username", "전화번호", "주소", "문의사항")

admin.site.register(models.User, CustomUserAdmin)
