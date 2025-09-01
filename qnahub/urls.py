from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='qnahub-home'),
    path('/question/<int:question_id>/', views.question_detail, name='qnahub-question-detail'),
]