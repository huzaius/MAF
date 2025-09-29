from django.urls import path
from .views import QuestionListView ,QuestionDetailView



urlpatterns = [
    path('', QuestionListView.as_view(), name='qnahub-home'),
    path('question/<int:pk>/',QuestionDetailView.as_view(), name='qnahub-question-detail'),

]