from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormMixin

from qnahub.forms import AnswerForm, QuestionForm
from .models import Question, Answer
from django.urls import reverse_lazy



class QuestionListView(ListView):
    model = Question
    template_name = 'qnahub/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'questions'
    ordering = ['-timestamp']
    paginate_by = 5


class QuestionDetailView(LoginRequiredMixin, FormMixin, DetailView):
    model = Question
    form_class = AnswerForm

    def get_success_url(self):
        return reverse_lazy('qnahub-question-detail', kwargs={'pk': self.get_object().pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.question = self.get_object()
        form.save() # have to save the form to create the Answer instance since using FormMixin
        return super().form_valid(form)
       
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
