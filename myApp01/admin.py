from django.contrib import admin

# Register your models here.
from myApp01.models import Board
from myApp01.models import User


admin.site.register(Board)
admin.site.register(User)