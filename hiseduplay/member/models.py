from django.db import models


class Member(models.Model):
    memberID = models.CharField(max_length=15, verbose_name="User ID", primary_key=True)
    nickname = models.CharField(max_length=30, verbose_name="Nickname")
    password = models.CharField(max_length=128, verbose_name="Password")
    name_mem = models.CharField(max_length=30, verbose_name="Name")
    email = models.EmailField(max_length=30, verbose_name="Email")
    register_dttm = models.DateTimeField(auto_now_add=True, verbose_name="Registered at")
    point = models.IntegerField(verbose_name="Point")

    def __str__(self):
        return self.nickname

    class Meta:
        managed = False
        db_table = "MEMBER"
