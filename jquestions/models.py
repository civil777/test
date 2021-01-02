from django.db import models
from core import models as core_models


class Jquestion(core_models.TimeStampedModel):
    subject = models.CharField(max_length=60)
    content = models.TextField()
    nickname = models.CharField(max_length=20)


    def __str__(self):
        return self.subject


class Answer(models.Model):
    question = models.ForeignKey(Jquestion, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()



