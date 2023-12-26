from django.db import models
from member.models import Member

# Create your models here.

class Question(models.Model):
    subject = models.CharField(max_length=200)
    content_q = models.TextField()
    create_dttm = models.DateTimeField()
    memberID = models.ForeignKey(Member, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'QUESTION'

class Answer(models.Model):
    content_a = models.TextField()
    create_dttm = models.DateTimeField()
    questionID = models.ForeignKey(Question, on_delete=models.CASCADE)
    writerID = models.CharField(max_length=15)
    
    class Meta:
        db_table = 'ANSWER'