from django.contrib import admin
from .models import Jquestion, Answer


@admin.register(Jquestion)
class JquAdmin(admin.ModelAdmin):

    list_display = ("subject", "created", "nickname",)

@admin.register(Answer)
class JanswerAdmin(admin.ModelAdmin):

    list_display = ("question", "create_date", "content", )



