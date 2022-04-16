from cProfile import label
from django import forms

class PostForm(forms.Form):
    title = forms.CharField(label='タイトル',max_length=30)
    deadline = forms.DateField(label='締切',max_length=30)