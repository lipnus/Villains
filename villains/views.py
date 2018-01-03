from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import redirect


def index(request):
    return render(request, "villains/default.html", {})
    # return render(request, "villains/default.html", {})
