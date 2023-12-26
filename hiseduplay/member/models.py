from django.db import models

# Create your models here.

class Member(models.Model):
    memberID = models.CharField(max_length=15, verbose_name='아이디', primary_key=True)
    nickname = models.CharField(max_length=30, verbose_name='별명')
    password = models.CharField(max_length=15, verbose_name='비밀번호')
    name_mem = models.CharField(max_length=30, verbose_name='사용자명')
    email = models.EmailField(max_length=30, verbose_name='이메일')
    register_dttm = models.DateTimeField(auto_now_add=True, verbose_name='회원가입일자')
    point = models.IntegerField(verbose_name='포인트')
    
    def __str__(self):
        return self.nickname

    class Meta:
        managed = False
        db_table = 'MEMBER'