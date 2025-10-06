from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from qnahub.forms import QuestionForm
from .models import Question, Answer
from django.urls import reverse_lazy



class QuestionListView(ListView):
    model = Question
    template_name = 'qnahub/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'questions'
    ordering = ['-timestamp']
    paginate_by = 5


class QuestionDetailView(DetailView):
    model = Question


class QuestionCreateView(LoginRequiredMixin, CreateView):
    model = Question
    form_class = QuestionForm
    # fields = ['title', 'content']     # Using form_class instead of fields to utilize QuestionForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('qnahub-question-detail', kwargs={'pk': self.object.pk})
    
class QuestionUpdateView(UpdateView):
    model = Question
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class QuestionDeleteView(DeleteView):
    model = Question
    success_url = reverse_lazy('qnahub-home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)    


class QuestionByUserListView(ListView):
    model = Question
    template_name = 'qnahub/user_questions.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'questions'
    paginate_by = 5

    def get_queryset(self):
        from django.contrib.auth.models import User
        user = User.objects.get(username=self.kwargs.get('username'))
        return Question.objects.filter(author=user).order_by('-timestamp')
    
class AnswerByUserListView(ListView):
    model = Answer
    template_name = 'qnahub/user_answers.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'answers'
    paginate_by = 5

    def get_queryset(self):
        from django.contrib.auth.models import User
        user = User.objects.get(username=self.kwargs.get('username'))
        return Answer.objects.filter(author=user).order_by('-timestamp')
