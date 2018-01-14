from django.forms import ModelForm
from .models import Villain
from django import forms

class VillainForm(ModelForm):
    class Meta:
        model = Villain
        widgets = {
            'villain_name': forms.TextInput(attrs={'placeholder': '홍길동'}),
            'univ': forms.TextInput(attrs={'placeholder': '고려대학교'}),
            'major': forms.TextInput(attrs={'placeholder': '컴퓨터학과'}),
            'class_name': forms.TextInput(attrs={'placeholder': '오징어심리학개론'}),
            'content': forms.Textarea(
                attrs={'placeholder': '그간의 만행을 적나라하게 적어주세요','class':'detail'}),
        }
        fields=['villain_name','univ','major','class_name','content','bomb']
