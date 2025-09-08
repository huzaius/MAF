from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from users import views as user_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('qnahub/', include('qnahub.urls')),
    path("",include('django.contrib.auth.urls')),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('account/', user_views.account, name='account'),
]
