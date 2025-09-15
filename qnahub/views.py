from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Question, Answer


def home_view(request):

    questions = Question.objects.all().order_by('-timestamp')
    context = {'questions': questions}
    return render(request, 'qnahub/home.html', context)


def question_detail_view(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'qnahub/question_detail.html', context)
