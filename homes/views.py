from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import generic
from . models import Question, Index, Test
from django.urls import reverse_lazy
from . forms import NameForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages


class TestView(generic.ListView):
    model = Test
    template_name = 'test_list.html'
    context_object_name = 'text'

class IndexView(generic.ListView):
    model = Index
    template_name = 'index_list.html'
    context_object_name = 'text'

class QuestionView(SuccessMessageMixin, generic.edit.CreateView):
    model = Question
    fields = [
    '이름',
    '전화번호',
    '이메일',
    '주소',
    '문의사항',]

    success_message = "문의하신 글이 성공적으로 등록되었습니다!"
    success_url = reverse_lazy('homes:index')
    template_name_suffix = '_create'







def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('homes:index')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'question_create.html', {'form': form})
