from django.shortcuts import render, render_to_response, get_object_or_404
from django.contrib import messages
import json

# Create your views here.

from .forms import UserForm, LoginForm
from django.contrib.auth.models import User

from django.http import HttpResponse
from django.shortcuts import redirect
from .forms import VillainForm, modifyForm
from .models import *
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST



def index(request):
    villains = Villain.objects.all()
    q = request.GET.get('searchText', '')
    searchType = request.GET.get('searchType')
    if q: # q가 있으면
        if searchType=="name":
            villains = villains.filter(villain_name__icontains=q) # 제목에 q가 포함되어 있는 레코드만 필터링
        elif searchType=="univ":
            villains = villains.filter(univ__icontains=q)
        elif searchType=="major":
            villains = villains.filter(major__icontains=q)
        elif searchType=="class_name":
            villains = villains.filter(class_name__icontains=q)
        elif searchType=="content":
            villains = villains.filter(content__icontains=q)
        return render(request, 'villains/default.html', {'villainList':villains} )
    else:
        villainList = Villain.objects.order_by('-update_date')[0:5]
        return render(request, 'villains/default.html', {'villainList':villainList} )
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
            return render_to_response('registration/login_error.html', {'form':form})
    else:
        form = LoginForm()
        return render(request, 'registration/login.html', {'form': form})


def signout(request):
    logout(request)
    return render(request, 'registration/logout.html', {})


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
            return render_to_response('registration/error.html', {'form':form})

    else:
        form = UserForm()
        return render(request, 'registration/adduser.html', {'form':form})


def register_villain(request):
    if request.method == "POST": #save update_date
        form = VillainForm(request.POST)
        if form.is_valid():

            villain = form.save(commit = False)
            villain.writter_id = request.user.get_username() #글쓴이는 auth와 연계하여 자동입력
            villain.generate()

            return redirect('index') #url에 있는 name입력하면 된다
    else:
        form = VillainForm()
        return render(request, "villains/register_villain.html", {"form":form})

def villain_detail(request,pk):
#참고1: https://wayhome25.github.io/django/2017/06/25/django-ajax-like-button/
#참고2: http://whatisthenext.tistory.com/121

    villain = get_object_or_404(Villain, pk=pk)
    villain_agree, villain_agree_created = villain.agree_set.get_or_create(user=request.user)

    if villain_agree_created: #생성되었다(눌렀던 적이 없음)
        villain_agree.delete()
        agree_ok = False
    else: #있던걸 꺼내왔다(눌렀었음)
        agree_ok = True

    return render(request, 'villains/villain_detail.html', {'villain': villain,"pk":pk, "agree_ok":agree_ok})

def villain_modify(request,pk):
    villain = get_object_or_404(Villain, pk=pk)
    if request.method == "POST": #save update_date
        form = modifyForm(request.POST,instance=villain)
        if form.is_valid():
            form.save() #변경내용을 저장
            return redirect('index') #url에 있는 name입력하면 된다
    else:
        form = modifyForm(instance=villain)
        return render(request, "villains/villain_modify.html", {'form':form})

@login_required
@require_POST # 해당 뷰는 POST method만 받는다.
def agree(request):
    pk = request.POST.get('pk', None) #빌런번호

    villain = get_object_or_404(Villain, pk=pk) #빌런객체
    villain_agree, villain_agree_created = villain.agree_set.get_or_create(user=request.user)

    if villain_agree_created: #처음 누르는 경우
        agree_ok = True
    else: #이미 눌렀던 경우
        villain_agree.delete()
        agree_ok = False

    villain.save()
    context = {'agree_count': villain.agree_count, 'agree_ok': agree_ok }

    return HttpResponse(json.dumps(context), content_type="application/json")


def delete(request,pk):
    villain = get_object_or_404(Villain, pk=pk)
    villain.delete()
    return redirect('index')

def villainSearch(request):
    q = request.GET.get('searchText','')
    searchType = request.GET.get('searchType')
    villains = Villain.objects.all()
    if q: # q가 있으면
        if searchType=="name":
            villains = villains.filter(villain_name__icontains=q) # 제목에 q가 포함되어 있는 레코드만 필터링
        elif searchType=="univ":
            villains = villains.filter(univ__icontains=q)
        elif searchType=="major":
            villains = villains.filter(major__icontains=q)
        elif searchType=="class_name":
            villains = villains.filter(class_name__icontains=q)
        elif searchType=="content":
            villains = villains.filter(content__icontains=q)

    
    s=[]
    for villain in villains:
        n={"name":villain.villain_name,"univ":villain.univ,"major":villain.major,"className":villain.class_name,"bomb":villain.bomb,"agree":villain.agree,"pk":villain.pk}
        s.append(n)
        
    result = s
    return HttpResponse(json.dumps(result), content_type="application/json")
