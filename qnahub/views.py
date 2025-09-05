from django.shortcuts import render, redirect
from django.http import Http404
from django.utils.timesince import timesince
from datetime import datetime, timezone
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomAuthenticationForm
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




def login_view(request):
    if request.user.is_authenticated:
        return redirect('qnahub-home')

    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('qnahub-home')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'qnahub/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('qnahub-home')


def register_view(request):
    if request.user.is_authenticated:
        return redirect('qnahub-home')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("qnahub-home")
        messages.error(
            request, "Unsuccessful registration. Invalid information.")
    else:
        form = CustomUserCreationForm()
    return render(request, 'qnahub/register.html', {'form': form})


def account_view(request):
    return render(request, 'qnahub/account.html')
