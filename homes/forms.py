from django import forms
from .models import Jquestion, Answer
class NameForm(forms.Form):
    이름 = forms.CharField(label='Your name', max_length=100)
    전화번호 = forms.CharField(label='전화번호', max_length=100)
    문의사항 = forms.CharField(label='문의사항', max_length=100)

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Jquestion
        fields = ['subject', 'content']

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }