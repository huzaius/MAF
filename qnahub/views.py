from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormMixin
from django.db.models import Max, F, Case, When, DateTimeField, Count
from django.shortcuts import redirect, get_object_or_404

from qnahub.forms import AnswerForm, QuestionForm
from .models import Question, Answer
from django.urls import reverse_lazy


class QuestionListView(ListView):
    model = Question
    template_name = 'qnahub/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'questions'
    paginate_by = 5

    def get_queryset(self):
        sort_option = self.request.GET.get('sort', 'newest')
        queryset = Question.objects.all()

        if sort_option == 'votes':
            # Annotate with the difference between upvotes and downvotes, then order by it.
            queryset = queryset.annotate(
                net_votes_count=Count('upvotes', distinct=True) - Count('downvotes', distinct=True)
            ).order_by('-net_votes_count', '-timestamp')
        elif sort_option == 'answers':
            # Annotate with the count of answers, then order by it.
            queryset = queryset.annotate(num_answers=Count('answers')).order_by('-num_answers', '-timestamp')
        else: # Default to 'newest'
            # Annotate with the latest activity (new answer or new question)
            queryset = queryset.annotate(latest_answer_time=Max('answers__timestamp'))
            queryset = queryset.annotate(
                last_activity=Case(
                    When(latest_answer_time__isnull=False, then=F('latest_answer_time')),
                    default=F('timestamp'),
                    output_field=DateTimeField()
                )
            )
            queryset = queryset.order_by('-last_activity')
        
        return queryset


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
       
class QuestionUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Question
    form_class = QuestionForm

    def get_success_url(self):
        return reverse_lazy('qnahub-question-detail', kwargs={'pk': self.object.pk})
    
    def test_func(self):
        question = self.get_object()
        return self.request.user == question.author

class QuestionDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Question
    success_url = reverse_lazy('qnahub-home')

    def test_func(self):
        question = self.get_object()
        return self.request.user == question.author

class AnswerUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Answer
    form_class = AnswerForm
    template_name = 'qnahub/answer_update_form.html'
    def get_success_url(self):
        return reverse_lazy('qnahub-question-detail', kwargs={'pk': self.object.question.pk})

    def test_func(self):
        answer = self.get_object()
        return self.request.user == answer.author

class AcceptAnswerView(LoginRequiredMixin, View):
    def post(self, request, pk):
        answer = get_object_or_404(Answer, pk=pk)
        question = answer.question

        if request.user != question.author:
            # This user is not the author of the question, so they can't accept an answer.
            # We can just redirect them back without doing anything.
            return redirect('qnahub-question-detail', pk=question.pk)

        if answer.accepted:
            # If it's already accepted, un-accept it.
            answer.accepted = False
            answer.save()
        else:
            # Un-accept any other accepted answer for this question first
            question.answers.filter(accepted=True).update(accepted=False)
            # Accept the new answer
            answer.accepted = True
            answer.save()

        return redirect('qnahub-question-detail', pk=question.pk)

class QuestionVoteView(LoginRequiredMixin, View):
    def post(self, request, pk):
        question = get_object_or_404(Question, pk=pk)
        vote_type = request.POST.get('vote_type')
        user = request.user

        if vote_type == 'up':
            if user in question.downvotes.all():
                question.downvotes.remove(user)
            
            if user in question.upvotes.all():
                question.upvotes.remove(user)
            else:
                question.upvotes.add(user)

        elif vote_type == 'down':
            if user in question.upvotes.all():
                question.upvotes.remove(user)

            if user in question.downvotes.all():
                question.downvotes.remove(user)
            else:
                question.downvotes.add(user)
        
        return redirect('qnahub-question-detail', pk=question.pk)

class AnswerVoteView(LoginRequiredMixin, View):
    def post(self, request, pk):
        answer = get_object_or_404(Answer, pk=pk)
        vote_type = request.POST.get('vote_type')
        user = request.user

        # Simplified toggle logic
        is_upvoted = user in answer.upvotes.all()
        is_downvoted = user in answer.downvotes.all()

        if vote_type == 'up':
            answer.upvotes.remove(user) if is_upvoted else answer.upvotes.add(user)
            if is_downvoted: answer.downvotes.remove(user)
        elif vote_type == 'down':
            answer.downvotes.remove(user) if is_downvoted else answer.downvotes.add(user)
            if is_upvoted: answer.upvotes.remove(user)
        
        return redirect('qnahub-question-detail', pk=answer.question.pk)



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

class AnswerDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Answer

    def get_success_url(self):
        return reverse_lazy('qnahub-question-detail', kwargs={'pk': self.object.question.pk})

    def test_func(self):
        answer = self.get_object()
        return self.request.user == answer.author
