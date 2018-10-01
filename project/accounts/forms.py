from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import PasswordChangeForm
from .models import User


class RegistrationForm(UserCreationForm):
    """
    ユーザ登録フォーム
    """

    last_name = forms.CharField(max_length=10, required=True)
    first_name = forms.CharField(max_length=10, required=True)

    class Meta:
        model = User
        fields = ['last_name', 'first_name', 'email']
        widgets = {
            'password': forms.PasswordInput()
        }

    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label


class LoginForm(forms.ModelForm):
    """
    ログインフォーム
    """

    class Meta:
        model = User
        fields = ('email', 'password')
        widgets = {
            'password': forms.PasswordInput()
        }

    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class MyPasswordChangeForm(PasswordChangeForm):
    """
    パスワード変更フォーム
    """

    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
