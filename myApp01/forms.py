from django.forms import ModelForm
from .models import *


class writeForm(ModelForm):
    class Meta:
        model = Board
        fields = ['title','id','content']

class signUpForm(ModelForm):
    class Meta:
        model = User
        fields = ['id','passwd','email','name','address']
