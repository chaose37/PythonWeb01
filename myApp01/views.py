from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Board,User

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

# Create your views here.
