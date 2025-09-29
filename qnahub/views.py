from django.shortcuts import render, redirect,get_object_or_404
from django.views.generic import ListView
from .models import Question, Answer




class QuestionListView(ListView):
    model = Question
    template_name = 'qnahub/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'questions'
    ordering = ['-timestamp']
    paginate_by = 5


class QuestionDetailView(ListView):
    model = Question
    template_name = 'qnahub/question_detail.html'
    context_object_name = 'question'
    




