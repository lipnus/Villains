from django.db import models

# Create your models here.
from django.utils import timezone
from django.db.models import IntegerField, Model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from django.conf import settings

class Villain(models.Model):
    writter_id = models.CharField(max_length = 24) # models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
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
    # agree_count = models.IntegerField(default=0) #인정
    content = models.CharField(max_length = 3000) #본문내용
    update_date = models.DateTimeField(auto_now=True) #자동으로 현재시간 추가

    agree_user_set = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                        blank=True,
                                        related_name='agree_user_set',
                                        through='Agree')

    @property
    def agree_count(self):
      return self.agree_user_set.count()


    #날짜생성 후 데이터베이스 저장
    def generate(self):
        self.update_date = timezone.now()
        self.save()  #Object를 데이터베이스에 저장

    # admin페이지에서 미리보기
    def __str__(self):
        return "빌런:%s (%s)" % (self.villain_name, self.update_date)


class Agree(models.Model):
    villain = models.ForeignKey(Villain, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return "%s가 %s글에 인정 누름" % (self.user, self.villain)
