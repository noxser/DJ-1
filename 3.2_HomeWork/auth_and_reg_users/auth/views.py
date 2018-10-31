from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, UserRegistrationForm


def home(request):
    # можно и в шаблоне получить user-а но тут в одном месте удобней
    cur_user = request.user
    context = {}
    if cur_user is not None:
        if cur_user.is_authenticated:
            context['cur_user'] = cur_user
        else:
            context['cur_user'] = False
    return render(
        request,
        'home.html', {'context': context}
    )


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})


def login_in(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return home(request)
                else:
                    return render(request, 'account/login_in.html', {'form': form, 'error': 'Аккаунт отключен'})
            else:
                return render(request, 'account/login_in.html', {'form': form, 'error': 'Не верный логин или пароль!'})
    else:
        form = LoginForm()
    return render(request, 'account/login_in.html', {'form': form})


def logged_out(request):
    logout(request)
    return render(
        request,
        'account/logged_out.html'
    )
