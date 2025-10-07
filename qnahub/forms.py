

from django import forms
from qnahub.models import Question ,Answer


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'input input-bordered rounded-lg w-full text-lg p-3', 'placeholder': 'e.g., How do I center a div in CSS?'}),
            'content': forms.Textarea(attrs={'class': 'textarea textarea-bordered rounded-lg w-full h-40 text-lg p-3', 'placeholder': "Include all the information someone would need to answer your question"}),
        }
        labels = {
            'title': 'Title',
            'content': 'Content',
        }
        help_texts = {
            'title': 'Be specific and imagine you\'re asking a question to another person.',
            'content': 'Include all the information someone would need to answer your question.',
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'textarea textarea-bordered rounded-lg w-full h-40 text-lg p-3', 'placeholder': "Write your detailed answer here..."}),
        }
        labels = {
            'content': 'Edit Answer',
        }
        help_texts = {
            'content': 'Provide a detailed answer to the question.',
        }
        