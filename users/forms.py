from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email','first_name','last_name']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_picture', 'phone_number', 'address', 'zip_code', 'city','state']
        widgets = {
            'profile_picture': forms.ClearableFileInput(attrs={'class': 'file-input file-input-bordered w-full max-w-xs'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['profile_picture'].label = ""


class AccountDeleteForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")
