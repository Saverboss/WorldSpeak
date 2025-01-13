from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegistrationForm, LoginForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Автоматический вход после регистрации
            messages.success(request, 'Регистрация прошла успешно!')
            return redirect('core:profile') # Перенаправление на страницу профиля
        else:
            for error in form.errors.values():
                messages.error(request, error.as_text())
    else:
        form = RegistrationForm()
    return render(request, 'core/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Вход выполнен успешно!')
                return redirect('core:profile')
            else:
                messages.error(request, 'Неверное имя пользователя или пароль.')
        else:
            for error in form.errors.values():
                messages.error(request, error.as_text())
    else:
        form = LoginForm()
    return render(request, 'core/login.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'core/profile.html', {'user': request.user})

def user_logout(request):
    logout(request)
    return redirect('core:login')