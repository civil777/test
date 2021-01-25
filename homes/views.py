from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import generic
from . models import Question, Test, T1, T2, T3, T4, T5, Q1, Q2, W1, W2, Rooma, Naver
from django.urls import reverse_lazy
from . forms import NameForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages



class TestView(generic.ListView):
    model = Test
    template_name = 'test_list.html'
    context_object_name = "homes"

class T1View(generic.ListView):
    model = T1
    template_name = 't1_list.html'
class T2View(generic.ListView):
    model = T2
    template_name = 't2_list.html'
class T3View(generic.ListView):
    model = T3
    template_name = 't3_list.html'
class T4View(generic.ListView):
    model = T4
    template_name = 't4_list.html'
class T5View(generic.ListView):
    model = T5
    template_name = 't5_list.html'

class Q1View(generic.ListView):
    model = Q1
    template_name = 'q1_list.html'

class Q2View(generic.ListView):
    model = Q2
    template_name = 'q2_list.html'

class W1View(generic.ListView):
    model = W1
    template_name = 'w1_list.html'
class W2View(generic.ListView):
    model = W2
    template_name = 'w2_list.html'

class NaverView(generic.ListView):
    model = Naver
    template_name = 'navera8e96fadc9fb10ede2d47018716d41fd.html'

class Naver1View(generic.ListView):
    model = Naver
    template_name = 'naverc9ad0d400160eac802e73eabe87309e9.html'

class IndexView(generic.ListView):
    model = Rooma
    template_name = 'index_list.html'
    context_object_name = "homes"


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
