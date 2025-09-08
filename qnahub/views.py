from django.shortcuts import render, redirect
from django.http import Http404
from .models import Question, Answer


def home_view(request):

    questions = Question.objects.all().order_by('-timestamp')
    context = {'questions': questions}
    return render(request, 'qnahub/home.html', context)


def question_detail_view(request, question_id):
    all_questions = Question.objects.all()
    question = next((q for q in all_questions if q['id'] == question_id), None)

    if not question:
        raise Http404("Question not found")

    context = {'question': question}
    return render(request, 'qnahub/question_detail.html', context)



