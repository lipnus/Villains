from django.db import models

# Create your models here.
from django.utils import timezone
from django.db.models import IntegerField, Model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
# from django.conf import settings

class Villain(models.Model):
    writter_id = models.OneToOneField(User, on_delete=models.CASCADE) # models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    villain_name = models.CharField(max_length = 24)
    univ = models.CharField(max_length = 24)
    major = models.CharField(max_length = 24)
    class_name = models.CharField(max_length = 24)
    bomb = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )
    content = models.CharField(max_length = 3000)
    update_date = models.DateTimeField(auto_now=True) #자동으로 현재시간 추가


    #날짜생성 후 데이터베이스 저장
    def generate(self):
        self.update_date = timezone.now()
        self.save()  #Object를 데이터베이스에 저장

    # admin페이지에서 미리보기
    def __str__(self):
        return "빌런:%s, 글쓴이:%s" % (self.villain_name, self.writter_id)