from django.contrib import admin

# Register your models here.
from villains.models import Villain

#관리창에서 등록할 수 있게 함
admin.site.register(Villain)
