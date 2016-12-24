from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from .models import *
from .forms import *


def index(req):
    msg = "My Message"
    return render(req,'index.html',{'msg':msg})

def board_table(req):
    return render(req,"board_basic.html",{'boardList':Board.objects.all()})


def board_Json(req):
    board_List = Board.objects.all();
    jsonList = []
    for board in board_List:
        jsonList.append({
            "bno":board.bno,
            "title":board.title,
            "content":board.content,
            "createDate":board.createDate,
            "updateDate":board.updateDate
        })
    return JsonResponse(jsonList,safe=False)

def createBoard(req):
    if req.method=="POST":
        form = writeForm(req.POST)
        if form.is_valid():
            form.save()
        return redirect("/board")
    else:
        form = writeForm()

    return render(req, "write_form.html",{"form":form})
