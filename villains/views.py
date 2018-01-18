from django.shortcuts import render, redirect
from django.http import HttpResponse

from django import forms

from .forms import UserForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.template import RequestContext, loader


def index(request):
    return HttpResponse('index 페이지입니다.')
    # return render(request, "villains/default.html", {})

def signin(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return HttpResponse('로그인 실패. 다시 시도 해보세요.')
    else:
        form = LoginForm()
        return render(request, 'registration/login.html', {'form': form})

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)

        if form.is_valid():
            new_user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
            )
            return redirect('index')
        else:   
            form = UserForm()
            return render(request, 'registration/adduser.html', {'form':form})

    else:
        form = UserForm()
        return render(request, 'registration/adduser.html', {'form':form})