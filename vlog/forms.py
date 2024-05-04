from django import forms
from .models import vlog
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):

    class Meta:
        model=User
        fields=(
            'username',
            'email',
            'password1',
            'password2',
        )

class VlogForm(forms.ModelForm):
    class Meta:
        model=vlog
        fields=('__all__')
