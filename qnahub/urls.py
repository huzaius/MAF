from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_view, name='qnahub-home'),
    path('question/<int:question_id>/', views.question_detail_view, name='qnahub-question-detail'),

]