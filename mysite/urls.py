"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf.urls import url
from villains import views


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),


    url(r'^login/', views.signin, name='login'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^join/', views.signup, name='join'),

    url(r'^register_villain/$', views.register_villain, name='register_villain'), #등록
    url(r'^detail/(?P<pk>[0-9]+)/$', views.villain_detail, name='villain_detail'), #상세보기
    url(r'^modify/(?P<pk>[0-9]+)/$', views.villain_modify, name='villain_modify'),
    url(r'^agree$', views.agree, name='agree'),
    url(r'^delete/(?P<pk>[0-9]+)/$', views.delete, name='villain_delete'),

]
