

from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate,logout
from django.contrib import messages
from .forms import RegisterForm , LoginForm
from django.contrib.auth.decorators import login_required



def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Hesabınız uğurla yaradıldı')    
            return redirect('user:login')
    else:
        form = RegisterForm()

    context = {'form': form}
    return render(request, 'register.html', context)

def login(request):
    context= {}
    context['form'] = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                auth_login(request, user)
                print('User is here!!!')
                return redirect('index')

            print('===================')

    return render(request, 'login.html', context)


def Logout(request):
    logout(request)
    messages.success(request,'Uğurla logout oldunuz...')
    return redirect('index')
    

