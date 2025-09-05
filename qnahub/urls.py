from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_view, name='qnahub-home'),
    path('question/<int:question_id>/', views.question_detail_view, name='qnahub-question-detail'),
    path('login/', views.login_view, name='qnahub-login'),
    path('logout/', views.logout_view, name='qnahub-logout'),
    path('register/', views.register_view, name='qnahub-register'),
    path('account/', views.account_view, name='qnahub-account'),

]