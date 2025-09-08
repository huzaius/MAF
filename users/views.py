from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from users.forms import UserRegisterForm

# Create your views here.
def register(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request,user)
            messages.success(request, f'Account created for {username}!')
            return redirect('qnahub-home')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html',{'form':form})


@login_required
def account(request):
    return render(request, 'users/account.html',{'user':request.user})