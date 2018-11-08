from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


def validate_even(value):
    """Длина пароля не менее 4 символов 1 буква 1 цифра
    """
    min_length = 4

    if len(value) < min_length:
        raise ValidationError(f'Пароль должен быть не менее {min_length} символов.')

    if not any(char.isdigit() for char in value):
        raise ValidationError('Пароль должен содержать хотя бы 1 цифру.')

    if not any(char.isalpha() for char in value):
        raise ValidationError('Пароль должен содержать хотя бы 1 букву.')


class LoginForm(forms.Form):
    username = forms.CharField(label="Имя пользователя:")
    password = forms.CharField(label="Пароль:", widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Придумайте пароль:', widget=forms.PasswordInput, validators=[validate_even])
    password2 = forms.CharField(label='Подтвердите пароль:', widget=forms.PasswordInput)
    username = forms.CharField(label="Имя пользователя:")

    class Meta:
        model = User
        fields = ('username',)

    def clean_password2(self):
        cd = self.cleaned_data
        password = cd.get('password', None)
        password2 = cd.get('password2', None)
        if password and cd['password2']:
            if password != password2:
                raise forms.ValidationError('Пароли не совпадают')
        return cd['password2']
