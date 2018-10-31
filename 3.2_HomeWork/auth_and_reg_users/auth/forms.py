from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(label="Имя пользователя:")
    password = forms.CharField(label="Пароль:", widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Придумайте пароль:', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Подтвердите пароль:', widget=forms.PasswordInput)
    username = forms.CharField(label="Имя пользователя:")

    class Meta:
        model = User
        fields = ('username',)

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return cd['password2']