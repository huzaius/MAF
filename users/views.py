from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import login, get_user_model
from users.forms import AccountDeleteForm, ProfileUpdateForm, UserRegisterForm, UserUpdateForm
from users.models import UserProfile

# Create your views here.
def register_view(request):
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
def account_view(request):
    # Ensure a profile exists for the user.
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('account')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=profile) 

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'registration/account.html',context)


@login_required
def delete_account_view(request):
    form = AccountDeleteForm()
    if request.method == 'POST':
        form = AccountDeleteForm(request.POST)
        if form.is_valid():
            user = request.user
            password = form.cleaned_data.get('password')
            if user.check_password(password):
                user.delete()
                messages.success(request, 'Your account has been successfully deleted.')
                return redirect('qnahub-home')
            else:
                messages.error(request, 'Incorrect password. Please try again.')
    
    context = {'form': form}
    return render(request, 'registration/delete_account_confirm.html', context)
