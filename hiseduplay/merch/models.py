from django.db import models
from member.models import Member

# Create your models here.

class Merch(models.Model):
    name_mer = models.CharField(max_length=30)
    cost = models.IntegerField()
    kind = models.CharField(max_length=30)
    memberID = models.ForeignKey(Member, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nickname

    class Meta:
        db_table = 'MERCH'