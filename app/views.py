from django.shortcuts import render
from django.views import View
from django.views.generic import ListView , View
from .models import Todo
import datetime
import pandas as pd

# Create your views here.

class IndexView(View):
    def get(self,request,*args,**kwargs):
        todo_list = Todo.objects.all()
        return render(request,'app/index.html',{
            'todo_list':todo_list,
        })
