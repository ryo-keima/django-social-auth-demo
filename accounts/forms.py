from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import ModelForm

from .models import User


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
        )


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
        )


class LoginFrom(AuthenticationForm):

    class Meta:
        model = User
