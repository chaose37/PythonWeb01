from django.shortcuts import render
from django.http import HttpResponse


def index(req):
    msg = "My Message"
    return render(req,'index.html',{'msg':msg})
# Create your views here.
