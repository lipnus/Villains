from django.shortcuts import render
from django.contrib import messages

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import redirect
from .forms import VillainForm
from .models import *


def index(request):
    return render(request, "villains/index.html", {})

def test(request):
    return render(request, "villains/default.html", {})

# def register_villain(request):
    # return render(request, "villains/register_villain.html", {})

def register_villain(request):
    if request.method == "POST": #save update_date
        form = VillainForm(request.POST)
        if form.is_valid():
            form.save() #변경내용을 저장
            return redirect('index') #url에 있는 name입력하면 된다

    else:
        form = VillainForm()
        return render(request, "villains/register_villain.html", {"form":form})
