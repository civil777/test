from django import forms
from .models import Jquestion, Answer

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Jquestion
        fields = ['subject', 'nickname', 'content']
        labels = {
            'nkckname': '닉네임',
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }