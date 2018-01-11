from django.shortcuts import render
from django.contrib import messages

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import redirect
from .forms import VillainForm
from .models import *


def index(request):
    return render(request, "villains/default.html", {})
    # return render(request, "villains/default.html", {})

def register(request):
    if request.method=='POST':
        form = VillainForm(request.POST)
        if form.is_valid():
            newVillain=form.save()
            newVillain.writter_id = request.user.get_username()
            newVillain.generate()
            messages.info(request, '성공적으로 등록되었습니다!')
        else:
            messages.info(request, '등록에 실패하였습니다')
        return redirect('/')
    else:
        form = VillainForm()
 
    return render(request, 'villains/register_villain.html', {'form': form})


