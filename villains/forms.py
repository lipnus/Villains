from django.forms import ModelForm
from .models import Villain
from django import forms

from django.contrib.auth.models import User
from django.forms.fields import CharField


class UserForm(forms.ModelForm):
    verify_password = forms.CharField(label = '비밀번호 확인', widget = forms.PasswordInput)
    password = forms.CharField(label = '비밀번호', widget = forms.PasswordInput)


    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'verify_password']


    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('이미 사용중인 아이디입니다.')
        return username

    def clean_verify_password(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('verify_password')

        if not password1:
            raise forms.ValidationError("비밀번호를 입력하세요.")
        if not password2:
            raise forms.ValidationError("비밀번호 확인란을 입력하세요.")
        if password1 != password2:
            raise forms.ValidationError("비밀번호가 일치하지 않습니다.")

        return password2

    def signup(self):
        if self.is_valid():
            return User.objects.create_user(username=self.cleaned_data['username'], password=self.cleaned_data['verify_password'])


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class VillainForm(ModelForm):
    class Meta:
        model = Villain
        widgets = {
            'villain_name': forms.TextInput(attrs={'placeholder': '홍길동'}),
            'univ': forms.TextInput(attrs={'placeholder': '학교'}),
            'major': forms.TextInput(attrs={'placeholder': '컴퓨터학과'}),
            'class_name': forms.TextInput(attrs={'placeholder': '오징어심리학개론'}),
            'content': forms.Textarea(attrs={'placeholder': '그간의 만행을 적나라하게 적어주세요','class':'detail'}),
        }
        fields=['villain_name','univ','major','class_name','content','bomb']

class modifyForm(ModelForm):
    class Meta:
        model = Villain
        widgets = {
            'villain_name': forms.TextInput(attrs={'placeholder': model.villain_name}),
            'univ': forms.TextInput(attrs={'placeholder': model.univ}),
            'major': forms.TextInput(attrs={'placeholder': model.major}),
            'class_name': forms.TextInput(attrs={'placeholder': model.class_name}),
            'content': forms.Textarea(
                attrs={'placeholder': model.content,'class':'detail'}),
        }
        fields=['villain_name','univ','major','class_name','content','bomb']