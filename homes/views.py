from django.shortcuts import render
from django.views import generic
from . models import Question, Index
from django.urls import reverse_lazy

class IndexView(generic.ListView):
    model = Index
    template_name = 'index_list.html'
    context_object_name = 'text'

class QuestionView(generic.edit.CreateView):
    model = Question
    fields = [
    '이름',
    '전화번호',
    '이메일',
    '주소',
    '문의사항',]

    success_url = reverse_lazy('homes:index')
    template_name_suffix = '_create'
