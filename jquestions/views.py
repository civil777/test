from django.shortcuts import render, get_object_or_404, redirect
from .models import Jquestion, Answer
from django.utils import timezone
from .forms import QuestionForm, AnswerForm
from django.views import generic


class JqView(generic.ListView):

    """ HomeView Definition """

    model = Jquestion
    paginate_by = 10

    ordering = "-created"
    context_object_name = "jquestion_list"

def jqview(request):
    jquestion_list = Jquestion.objects.order_by('-created')
    context = {'jquestion_list': jquestion_list}
    return render(request, 'jquesionts/jquestion_list.html', context)

def detail(request, question_id):
    question = Jquestion.objects.get(id=question_id)
    context = {'question': question}
    return render(request, 'jquestions/jquestion_detail.html', context)

def answer_create(request, question_id):

    question = get_object_or_404(Jquestion, pk=question_id)
    question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())

def question_create(request):

    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('jquestions:jq')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'jquestions/jquestion_form.html', context)

def answer_create(request, question_id):

    question = get_object_or_404(Jquestion, pk=question_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('jquestions:detail', question_id=question_id)

        else:
            form = AnswerForm()
        context = {'question': question, 'form': form}
        return render(request, 'jquestions/jquestion_detail.html', context)

