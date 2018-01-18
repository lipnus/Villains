from django import forms
from django.contrib.auth.models import User
from django.forms.fields import CharField



class UserForm(forms.ModelForm):
	verify_password = forms.CharField(label = '비밀번호 확인', widget = forms.PasswordInput)
	password = forms.CharField(label = '비밀번호', widget = forms.PasswordInput)
    

	class Meta:
		model = User
		fields = ['username', 'email', 'password', 'verify_password']

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


"""
success = user.check_password(request.POST['submitted_password'])
if success: 
   # do your email changing magic
else:
   return http.HttpResponse("Your password is incorrect") 
   # or more appropriately your template with errors
"""

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
