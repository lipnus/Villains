from django.contrib import admin

# Register your models here.
from villains.models import Villain, Agree


#관리창에서 보이게 함
admin.site.register(Villain)
admin.site.register(Agree)
