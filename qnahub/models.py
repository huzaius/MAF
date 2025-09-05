from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='questions')
    title = models.CharField(max_length=255)
    content = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)
    upvotes = models.ManyToManyField(User, related_name='question_upvotes', blank=True)
    downvotes = models.ManyToManyField(User, related_name='question_downvotes', blank=True)

    def __str__(self):
        return self.title

    @property
    def net_votes(self):
        return self.upvotes.count() - self.downvotes.count()

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answers')
    content = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)
    accepted = models.BooleanField(default=False)
    upvotes = models.ManyToManyField(User, related_name='answer_upvotes', blank=True)
    downvotes = models.ManyToManyField(User, related_name='answer_downvotes', blank=True)

    def __str__(self):
        return f"Answer to '{self.question.title}' by {self.author.username}"

    @property
    def net_votes(self):
        return self.upvotes.count() - self.downvotes.count()
