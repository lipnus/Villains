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

def register_villain(request):
    return render(request, "villains/register_villain.html", {})
