from django.db import models

# Create your models here.
#以下クラスの継承

CHOICE = (('danger','high'),('warning','normal'),('primary','low'))

class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField()
    priority = models.CharField(
        max_length=50,
        choices = CHOICE
        )
    duedate = models.DateField()

    #Objectが作成された際に文字列情報を返していく
    def __str__(self):
        return self.title
