from django.contrib import admin
from . import models

@admin.register(models.Question)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("이름", "전화번호", "주소", "문의사항","created", )

