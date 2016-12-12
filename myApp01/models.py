from django.db import models

# Create your models here.

class User(models.Model):
    # 회원관리를 위한 모델
    id = models.CharField(max_length=30,primary_key=True)
    passwd = models.CharField(max_length=30)
    name = models.CharField(max_length=10)
    engName = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.TextField()
    createDate = models.DateTimeField(auto_now_add=True)
    lastLogingDate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.id


class Board(models.Model) :
    # 게시판 관리를 위한 모델
    # 파일과 댓글기능은 나중에 추가
    bno = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    id = models.CharField(max_length=30)
    content = models.TextField()
    createDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        self.title
