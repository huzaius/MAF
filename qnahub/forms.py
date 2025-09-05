from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms

class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'class': 'input input-bordered w-full', 'placeholder': 'Enter your username'}
        )
        self.fields['password'].widget.attrs.update(
            {'class': 'input input-bordered w-full', 'placeholder': 'Enter your password'}
        )

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True, 
        help_text='Required. Enter a valid email address.',
        widget=forms.EmailInput(attrs={'class': 'input input-bordered w-full', 'placeholder': 'email@example.com'})
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'input input-bordered w-full'
            if field_name == 'password1':
                field.widget.attrs['placeholder'] = 'Enter your password'
            if field_name == 'password2':
                field.widget.attrs['placeholder'] = 'Confirm your password'