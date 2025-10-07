from django.urls import path
from .views import QuestionCreateView, QuestionListView ,QuestionDetailView, QuestionUpdateView, QuestionDeleteView, QuestionByUserListView, AnswerByUserListView, AnswerUpdateView, AnswerDeleteView




urlpatterns = [
    path('', QuestionListView.as_view(), name='qnahub-home'),
    path('question/<int:pk>/',QuestionDetailView.as_view(), name='qnahub-question-detail'),
    path('question/new/', QuestionCreateView.as_view(), name='qnahub-question-create'),
    path('question/<int:pk>/update/', QuestionUpdateView.as_view(), name='qnahub-question-update'),
    path('question/<int:pk>/delete/', QuestionDeleteView.as_view(), name='qnahub-question-delete'),
    path('answer/<int:pk>/update/', AnswerUpdateView.as_view(), name='qnahub-answer-update'),
    path('answer/<int:pk>/delete/', AnswerDeleteView.as_view(), name='qnahub-answer-delete'),
    # path('user/<str:username>/', QuestionByUserListView.as_view(), name='user-questions'),
    # path('user/<str:username>/answers/', AnswerByUserListView.as_view(), name='user-answers'),    
]