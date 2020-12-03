from django.shortcuts import render
from django.views import generic
from . models import Question

class IndexView(generic.ListView):
    model = Question
    template_name = 'question_list.html'
    context_object_name = 'text'
# Create your views here.
