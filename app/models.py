from email.policy import default
from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Todo(models.Model):
    title = models.CharField("タイトル",max_length=30)
    deadline = models.DateField("締切")
    complite = models.DateField("完了日",blank=True,null=True)
    created = models.DateTimeField("作成日",default=timezone.now)

    def __str__(self):
        return self.title