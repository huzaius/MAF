from django.urls import path

from . import views as user_views

urlpatterns = [
    path('register/', user_views.register_view, name='register'),
    path('account/', user_views.account_view, name='account'),
    path('account/delete/', user_views.delete_account_view, name='delete_account'),
   ]